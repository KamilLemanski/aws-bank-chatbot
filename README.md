**Chatbot Concept Bank Polska**

Live App ➤ https://cbp-strona-chatbot-us.s3.us-east-1.amazonaws.com/index.html

Chatbot Concept Bank Polska to zaawansowane rozwiązanie typu konwersacyjnej AI, pełniące rolę wirtualnego doradcy klienta dla fikcyjnej instytucji bankowej. Jego nadrzędnym celem jest zapewnienie natychmiastowego dostępu do precyzyjnych i spójnych informacji o ofercie banku, działając w modelu 24/7 bez konieczności interwencji człowieka.

Aplikacja została zaprojektowana i wdrożona w oparciu o nowoczesną, w pełni serverless architekturę na platformie Amazon Web Services (AWS), co gwarantuje wysoką skalowalność, optymalizację kosztów oraz minimalizację prac administracyjnych.

Sercem systemu jest usługa Amazon Bedrock, która dostarcza zaawansowane modele językowe (LLM). W projekcie zaimplementowano mechanizm Retrieval-Augmented Generation (RAG), który pozwala chatbotowi na udzielanie odpowiedzi bazujących wyłącznie na zweryfikowanej, wewnętrznej bazie wiedzy (dokumentach z ofertą banku).

Kluczowe komponenty architektury to Amazon S3, Titan Text Embeddings V2, AWS Lambda, Claude 3 Sonnet oraz Amazon API Gateway.
Chatbot Concept Bank Polska stanowi w pełni funkcjonalny prototyp zautomatyzowanego centrum obsługi klienta, zdolnego do dynamicznego adaptowania się do zmian w ofercie poprzez prostą aktualizację bazy dokumentów.
Aplikacja została przygotowana w całości w regionie AWS us-east-1 (Northern Virginia).

------------
✨ Właściwości:

🗣️ Konwersacyjne AI (chatbot rozumie i odpowiada na pytania zadawane językiem naturalnym)

📚 Odpowiedzi oparte na wiedzy (wszystkie odpowiedzi generowane są na podstawie załączonych dokumentów banku: regulaminu, oferty kont osobistych oraz FAQ)

⚡ Dostępność 24/7 (wsparcie bez przerw)

☁️ Architektura serwerless (aplikacja w pełni oparta na skalowalnych i zarządzanych usługach AWS)

🖥️ Nowoczesny interfejs użytkownika (prosty i intuicyjny interfejs czatu)

🔒 Bezpieczeństwo i prywatność (interakcje z chatbotem są przetwarzane w bezpiecznym środowisku AWS)

------------
🧪 Zastosowane technologie:

Amazon S3: Hosting statycznej strony internetowej (frontend) oraz przechowywanie dokumentów bazowych dla AI.

AWS Lambda: Backend aplikacji (logika przetwarzania zapytań użytkownika).

Amazon Bedrock: platforma do budowania aplikacji opartych na generatywnej sztucznej inteligencj

Amazon API Gateway: Tworzy punkt końcowy API, który łączy frontend z funkcją Lambda.

Claude 3 Sonnet: model LLM wykorzystany do generowania odpowiedzi chatbota.

Titan Text Embeddings V2: model językowy, który konwertuje przygotowany tekst na reprezentacje numeryczne/wektory numeryczne (embeddingi).

Frontend: HTML, CSS, JavaScript.

Google Gemini 2.5 Pro: do stworzenia grafiki logo banku.

------------
🧠 Architektura Aplikacji:

Aplikacja działa w modelu serwerless, gdzie poszczególne usługi AWS odpowiadają za konkretne zadania, tworząc spójny i wydajny system RAG (Retrieval-Augmented Generation).

Frontend (S3): Użytkownik wprowadza zapytanie w interfejsie webowym aplikacji hostowanej na Amazon S3.

Wysłanie zapytania (API Gateway): Skrypt JavaScript wysyła zapytanie użytkownika do punktu końcowego API Gateway.

Przetwarzanie (AWS Lambda): API Gateway uruchamia funkcję Lambda, przekazując jej treść zapytania.

Generowanie odpowiedzi (Amazon Bedrock: Claude 3 Sonnet, Titan Text Embeddings V2): Funkcja Lambda komunikuje się z usługą Amazon Bedrock. Bedrock wykorzystuje swoją bazę wiedzy (stworzoną z dokumentów .txt) do znalezienia odpowiednich informacji i generowania precyzyjnej odpowiedzi.

Zwrot odpowiedzi: Wygenerowana odpowiedź jest zwracana przez API Gateway do frontendu i wyświetlana użytkownikowi w oknie czatu.

------------
👉 Uruchomienie aplikacji online:

https://cbp-strona-chatbot-us.s3.us-east-1.amazonaws.com/index.html

------------
📂 Struktura plików:

chatbot-concept-bank-polska/
<br>
<br>
<br>

cbp-chatbot-data-us/        # Bucket S3 na dane przetwarzane przez AI

CBP_chunks_all.json             # Plik z dokumentacją banku podzieloną na małe fragmenty (chunki)

CBP_chunks+embedded.json             # Chunks z dodanymi do nich wektorami numerycznymi (embeddings)

CBP_FAQ.txt             # Wersja tekstowa dokumentu FAQ do przetwarzania

CBP_Oferta_kont_Osobistych.txt             # Wersja tekstowa oferty do przetwarzania

CBP_Regulamin.txt             # Wersja tekstowa regulaminu do przetwarzania
<br>
<br>
<br>

lambda/

GenerateCBPEmbeddings.py # Skrypt do generowania wektorów (embeddings) z chunków tekstowych

CBPChatbotFileLoader.py # Skrypt do ładowania i wstępnego przetwarzania plików źródłowych

CBPBedrockChat.py # Kod głównej funkcji AWS Lambda (backend)
<br>
<br>
<br>

cbp-strona-chatbot-us/ # Bucket S3 na pliki statycznej strony internetowej

CBP FAQ.pdf # pdf FAQ do wglądu i pobrania

CBP Oferta Kont Osobistych.pdf # pdf oferty kont do wglądu i pobrania

CBP Regulamin.pdf # pdf regulaminu do wglądu i pobrania

CBP Tabela Opłat i Prowizji.pdf # pdf z podsumowaniem wszystkich cen

CBP_logo.png # Plik z logo banku wykorzystany na stronie

index.html # Główny plik HTML interfejsu użytkownika

------------
☁️ Wdrożenie aplikacji na platformie AWS w skrócie (10 kroków):

1. Stwórz bucket S3, przygotuj pliki backendu i wgraj je do bucketu.

2. Złóż wniosek o dostęp do potrzebnych modeli językowych AWS

3. Stwórz potrzebne funkcje AWS Lambda używając Pythona jako środowiska uruchomieniowego.

4. Wgraj kody oraz przeprowadź ich testy (sprawdź logi w Amazon CloudWatch)

5. Skonfiguruj rolę IAM dla funkcji Lambda, nadając jej uprawnienia do wywoływania modeli w usłudze Amazon Bedrock.

6. Stwórz bazę wiedzy w Amazon Bedrock, wskazując jako źródło danych bucket S3 zawierający dokumenty .txt.

7. Stwórz bucket S3 frontendu i skonfiguruj go do hostowania statycznej strony internetowej.

8. Przygotuj i prześlij pliki frontedu (index.html, logo, pliki pdf)

9. Stwórz API Gateway (np. HTTP API) i skonfiguruj integrację z wcześniej utworzoną funkcją Lambda.

10. W pliku index.html zaktualizuj adres URL punktu końcowego, aby wskazywał na Twoje API Gateway.

------------
📌 Przykład użycia:

Otwórz aplikację, klikając w link: https://cbp-strona-chatbot-us.s3.us-east-1.amazonaws.com/index.html.

W oknie czatu na dole ekranu wpisz pytanie dotyczące oferty Concept Bank Polska, np. "Jakie są opłaty za konto Concept Plus?".

Naciśnij klawisz Enter lub kliknij ikonę wysyłania.

Poczekaj chwilę na odpowiedź. Chatbot przeanalizuje Twoje pytanie i wygeneruje odpowiedź na podstawie załączonej dokumentacji bankowej.

------------
📝 Licencja:

© 2025 Kamil Lemański. Projekt stworzony w celach edukacyjnych i demonstracyjnych.

------------
🙏 Credits:

Amazon Web Services:
S3, Lambda, Amazon, Bedrock, API Gateway, Claude 3 Sonnet, Titan Text Embeddings V2

Google Gemini 2.5 Pro
