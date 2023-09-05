from dotenv import load_dotenv
import os
import deepl

load_dotenv()

deepLKey = os.environ.get('DEEPL-API-KEY')
translator = deepl.Translator(deepLKey)

input_path = "ch06.docx"
output_path = "ch06-translated.docx"
try:
    translator.translate_document_from_filepath(
        input_path,
        output_path,
        target_lang="KO"
    )

except deepl.DocumentTranslationException as error:
    doc_id = error.document_handle.id
    doc_key = error.document_handle.key
    print(f"에러 발생 ${error}, id: ${doc_id} key: ${doc_key}")
except deepl.DeepLException as error:
    print(error)