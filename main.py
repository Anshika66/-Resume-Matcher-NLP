from flask import Flask, render_template, request
import os
import PyPDF2
import docx2txt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


# ---------------- HELPER FUNCTIONS ----------------
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()
    return text


def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read()


def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)


def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    return ""


# ---------------- ROUTES ----------------
@app.route('/')
def home():
    return render_template('matchresume.html')


@app.route('/matcher', methods=['POST'])
def match_resumes():
    job_description = request.form.get('job_description')
    resume_files = request.files.getlist('resumes')

    if not job_description or not resume_files:
        return render_template('matchresume.html')

    resumes_text = []
    resume_names = []

    for file in resume_files:
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)

        text = extract_text(path)
        if text.strip():   # avoid empty resumes
            resumes_text.append(text)
            resume_names.append(filename)

    # -------- TF-IDF + COSINE SIMILARITY --------
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(
        [job_description] + resumes_text
    )

    similarity = cosine_similarity(vectors[0:1], vectors[1:])[0]

    # Top 3 matches
    top_indices = similarity.argsort()[-3:][::-1]

    top_resumes = [resume_names[i] for i in top_indices]
    similarity_scores = [round(similarity[i] * 100, 2) for i in top_indices]

    # PASS EXACT VARIABLES HTML EXPECTS
    return render_template(
        'matchresume.html',
        top_resumes=top_resumes,
        similarity_scores=similarity_scores
    )


# ---------------- RUN APP ----------------
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    app.run(debug=True)
