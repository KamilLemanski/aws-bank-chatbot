Chatbot Concept Bank Polska

Live App ➤ https://cbp-strona-chatbot-us.s3.us-east-1.amazonaws.com/index.html

Chatbot Concept Bank Polska to chatbot AI, który udziela odpowiedzi na pytania dotyczące oferty fikcyjnego banku. Aplikacja została zbudowana w oparciu o architekturę serwerless na platformie Amazon Web Services, wykorzystując model językowy z usługi Amazon Bedrock do rozumienia i odpowiadania na zapytania użytkowników w czasie rzeczywistym.

Celem projektu było stworzenie w pełni funkcjonalnego, opartego na dokumentacji, centrum obsługi klienta dostępnego 24/7.
Chatbot został w pełni wykonany z narzędzi Amazon Web Services: S3, AWS Lambda, Amazon Berdock, API Gateway, Claude 3 Sonnet i Titan Text Embeddings V2.

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

├── cbp-chatbot-data-us/       # Bucket S3 na dane przetwarzane przez AI       

│   ├── CBP_chunks_all.json    # Plik z dokumentacją banku podzieloną na małe fragmenty (chunki)

│   ├── CBP_chunks+embedded.json  # Chunks z dodanymi do nich wektorami numerycznymi (embeddings)

│   ├── CBP_FAQ.txt            # Wersja tekstowa dokumentu FAQ do przetwarzania

│   ├── CBP_Oferta_kont_Osobistych.txt  # Wersja tekstowa oferty do przetwarzania

│   ├── CBP_Regulamin.txt      # Wersja tekstowa regulaminu do przetwarzania

│

├── lambda/

│   ├── GenerateCBPEmbeddings.py  # Skrypt do generowania wektorów (embeddings) z chunków tekstowych

│   ├── CBPChatbotFileLoader.py   # Skrypt do ładowania i wstępnego przetwarzania plików źródłowych

│   └── CBPBedrockChat.py         # Kod głównej funkcji AWS Lambda (backend)

│

├── cbp-strona-chatbot-us/     # Bucket S3 na pliki statycznej strony internetowej 

    ├── CBP FAQ.pdf            # pdf FAQ do wglądu i pobrania
    
    ├── CBP Oferta Kont Osobistych.pdf # pdf oferty kont do wglądu i pobrania
    
    ├── CBP Regulamin.pdf      # pdf regulaminu do wglądu i pobrania
    
    ├── CBP Tabela Opłat i Prowizji.pdf #pdf z podsumowaniem wszystkich cen
    
    ├── CBP_logo.png            # Plik z logo banku wykorzystany na stronie
    
    └── index.html              # Główny plik HTML interfejsu użytkownika

------------
☁️ Wdrożenie na platformie AWS w skrócie:

Stwórz bucket S3 i skonfiguruj go do hostowania statycznej strony internetowej.

Wgraj pliki frontendu do bucketa S3.

Stwórz funkcje AWS Lambda używając Pythona jako środowiska uruchomieniowego i wgraj kod.

Skonfiguruj rolę IAM dla funkcji Lambda, nadając jej uprawnienia do wywoływania modeli w usłudze Amazon Bedrock.

Stwórz bazę wiedzy w Amazon Bedrock, wskazując jako źródło danych bucket S3 zawierający dokumenty .txt.

Stwórz API Gateway (np. HTTP API) i skonfiguruj integrację z wcześniej utworzoną funkcją Lambda.

W pliku index.html zaktualizuj adres URL punktu końcowego, aby wskazywał na Twoje API Gateway.

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
