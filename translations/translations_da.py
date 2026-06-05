
# ============================================
# translations_da.py - Dansk ordbog
# Fuldstændig sorteret efter kategorier
# Kommentarer på tysk for konsistens
# ============================================

def load_danish_strings():
    """Indlæser alle danske strenge"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View af BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Åbn PDF",
        'btn_text_window': "OCR-tekst",
        'btn_first': "Første side",
        'btn_prev': "Forrige side",
        'btn_next': "Næste side",
        'btn_last': "Sidste side",
        'btn_print': "Udskriv",
        'btn_darkmode_light': "Lys tilstand",
        'btn_darkmode_dark': "Mørk tilstand",
        'btn_delete_pages': "Slet sider",
        'btn_extract_pages': "Uddrag sider",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Annuller",
        'btn_save': "Gem",
        'btn_close': "Luk",
        'btn_delete': "Slet",
        'btn_delete_all': "Slet alle",
        'btn_copy': "Kopiér",
        'btn_export': "Eksporter",
        'btn_show': "Vis adgangskode",
        'btn_hide': "Skjul adgangskode",
        'btn_authenticate': "Godkend",
        'btn_settings': "Indstillinger",
        'btn_protect': "Beskyt",
        'btn_remove_password': "Fjern adgangskode",
        'btn_manage': "Adgangskodehåndtering",
        'btn_retry': "Prøv igen",
        'btn_select_all': "Vælg alle",
        'btn_clear_selection': "Fravælg",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Side {0} af {1}",
        'page_count': "af {0}",
        'goto_page': "Gå til side",
        'page_simple': "Side {0}",
        'full_view_page': "Fuld visning side {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Indtast søgeord + Enter",
        'search_results': "Resultater: {0} af {1}",
        'search_nav_hint': "Enter: næste  (Shift+Enter: forrige) resultat",
        'search_no_results': "Ingen resultater",
        'search_error': "Søgefejl",
        'search_active': "Søgefelt aktiveret",
        'search_closed': "Søgning afsluttet",
        'search_position': "Side {0} {1}",
        'search_pos_top': "øverst",
        'search_pos_upper': "øverst",
        'search_pos_middle': "midten",
        'search_pos_lower': "nederst",
        'search_pos_bottom': "nederst",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Tekstgenkendelse gennemført!",
        'ocr_success_title': "OCR lykkedes",
        'ocr_success_message': "Dokumentet er nu søgbart.",
        'ocr_failed': "OCR mislykkedes",
        'ocr_in_progress': "OCR i gang",
        'ocr_preparing': "Forbereder PDF...",
        'ocr_analyzing': "Analyserer PDF...",
        'ocr_optimizing': "Billedoptimering...",
        'ocr_recognizing': "Tekstgenkendelse...",
        'ocr_embedding': "Indlejrer tekst...",
        'ocr_finalizing': "Færdiggør PDF...",
        'ocr_not_available': "OCR ikke tilgængelig",
        'ocr_install_message': "OCR‑værktøjer blev ikke fundet.\n\nInstallér:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR påkrævet",
        'ocr_question': "PDF'en indeholder ingen søgbar tekst.\nVil du køre OCR for at muliggøre {0}?",
        'ocr_perform': "Kør OCR",
        'ocr_later': "Senere",
        'ocr_starting': "Starter garanteret OCR...",
        'ocr_success_voice': "OCR lykkedes. PDF er nu søgbar.",
        'ocr_partial_success': "OCR blev udført, men der opstod problemer under udskiftning.\n\nDen søgbare version blev gemt som:\n{0}\n\nFejl: {1}",
        'ocr_partial_title': "OCR delvist lykkedes",
        'ocr_partial_voice': "OCR udført, men udskiftning mislykkedes.",
        'original_file': "Original fil:",
        'old_size': "Gammel filstørrelse:    {0} bytes",
        'new_size': "Ny filstørrelse: {0} bytes",
        'size_change': "Ændring: {0}{1} bytes",
        'backup_created_file': "Backup oprettet:\n{0}",
        'backup_not_created': "Backup: ikke oprettet (indstilling deaktiveret)",
        'page_header': "=== Side {0} ===\n{1}\n",
        'scanned_page_header': "=== Side {0} (scannet) ===\n[Denne side indeholder kun scannet tekst]\n[Udfør OCR manuelt]\n",
        'scanned_warning': "⚠️ SCANNET TEKST - OCR PÅKRÆVET",
        'guaranteed_title': "Søgbar PDF oprettet",
        'guaranteed_message': "<b>Garanteret søgbar version oprettet!</b>\n\nDa automatisk OCR mislykkedes, blev en alternativ søgbar PDF oprettet:\n\n{0}\n\n<b>Denne fil indeholder:</b>\n• Udvundet tekst (hvis tilgængelig)\n• Henvisninger til scannede sider\n• Er fuldt søgbar",
        'guaranteed_voice': "Garanteret søgbar PDF oprettet.",
        'instruction_title': "VEJLEDNING TIL OCR",
        'instruction_file': "Original fil: {0}",
        'instruction_text': "Automatisk tekstgenkendelse (OCR) mislykkedes.\nUdfør OCR manuelt:\n\n1. MED OCRmyPDF (kommandolinje):\n   ocrmypdf --force-ocr \"[FIL]\" \"output.pdf\"\n\n2. MED ADOBE ACROBAT (macOS/Windows):\n   • Åbn PDF i Acrobat\n   • Værktøjer > Rediger PDF\n   • Vælg 'Genkend tekst'\n\n3. MED FORHÅNDSVISNING (macOS):\n   • Åbn PDF i Forhåndsvisning\n   • Arkiv > Eksportér...\n   • Quartz‑filter: 'Reduce File Size'\n   • Aktivér 'Udfør OCR'\n\n4. ONLINE OCR‑TJENESTER:\n   • smallpdf.com/da/ocr-pdf\n   • ilovepdf.com/da/ocr-pdf\n   • adobe.com/dk/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR‑vejledning oprettet",
        'instruction_created_message': "En detaljeret vejledning blev oprettet:\n\n{0}\n\nFølg trinnene for manuel OCR.",
        'instruction_created_voice': "OCR‑vejledning oprettet.",
        'ocr_impossible': "OCR ikke mulig",
        'ocr_impossible_message': "OCR kunne ikke udføres.\n\nBearbejd '{0}' manuelt med OCR‑software.",
        'ocr_impossible_voice': "OCR ikke mulig. Udfør manuel behandling.",
        'emergency_title': "Nød‑OCR",
        'emergency_message': "En nød‑PDF blev oprettet:\n\n{0}\n\nBearbejd denne fil manuelt med OCR.",
        'emergency_voice': "Nød‑PDF oprettet. Udfør OCR manuelt.",
        'critical_error': "Kritisk fejl",
        'critical_error_message': "OCR kunne ikke startes.\n\nGenstart programmet, og\ntjek OCR‑installationen.",
        'critical_error_voice': "Kritisk OCR‑fejl",
        'ocr_question_html': "<p>PDF'en indeholder ingen søgbar tekst.<p>Vil du køre OCR for at muliggøre <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR påkrævet. PDF'en indeholder ingen søgbar tekst. Vil du køre OCR for at muliggøre {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "ingen PDF indlæst",
        'no_pdf_message': "Der er ingen PDF indlæst",
        'pdf_not_found': "PDF‑fil ikke fundet",
        'file_size': "Filstørrelse",
        'bytes': "bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Backup oprettet",
        'backup_disabled': "Backup deaktiveret",
        'backup_activated': "Backup‑oprettelse aktiveret",
        'backup_deactivated': "Backup‑oprettelse deaktiveret",
        'backup_status': "Backup: {0}",
        'backup_on': "✔ aktiveret",
        'backup_off': "✘ deaktiveret",
        'close_pdf': "Lukker PDF: {0}",
        'pdf_not_found_format': "PDF‑fil ikke fundet: {0}",
        'error_pdf_load_format': "Fejl ved indlæsning af PDF: {0}",
        'load_failed_format': "Indlæsning mislykkedes:\n{0}",
        'decrypted_suffix': "(dekrypteret)",
        'decryption_failed': "Dekryptering mislykkedes.",
        'decryption_error': "Fejl under dekryptering",
        'decryption_success': "Dekryptering lykkedes",
        'decryption_success_message': "PDF blev dekrypteret og gemt som:\n\n{0}",
        'decryption_success_voice': "PDF blev dekrypteret og gemt.",
        'password_remove_error': "Fejl ved fjernelse af adgangskode",
        'save_unencrypted': "Gem ukrypteret PDF som",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Gem som...",
        'save_copy': "Gem kopi",
        'save_success': "PDF gemt som: {0}",
        'save_encrypted': "Beskyttet PDF gemt som: {0}",
        'save_error': "PDF kunne ikke gemmes",
        'encryption_question': "Vil du beskytte PDF'en med en adgangskode?",
        'encryption_yes': "Ja",
        'encryption_no': "Nej",
        'encryption_cancel': "Annuller",
        'save_cancel': "Gemning annulleret",
        'save_encrypted_voice': "Fil krypteret og gemt.",
        'save_success_voice': "PDF‑filen blev gemt ukrypteret.",
        'save_error_format': "PDF kunne ikke gemmes:\n{0}",
        'export_pages_success': "Pages‑eksport lykkedes",
        'export_pages_error': "Pages‑eksport mislykkedes",
        'export_pages_error_format': "Pages‑eksport mislykkedes: {0}",
        'export_word_success': "Word‑eksport lykkedes",
        'export_word_error': "Word‑eksport mislykkedes",
        'export_word_error_format': "Word‑eksport mislykkedes: {0}",
        'export_text_success': "Teksteksport lykkedes",
        'export_text_error': "Teksteksport mislykkedes",
        'export_text_error_format': "Teksteksport mislykkedes: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Adgangskode påkrævet",
        'password_enter': "Indtast adgangskode",
        'password_confirm': "Bekræft adgangskode",
        'password_new': "Ny adgangskode",
        'password_current': "Nuværende adgangskode",
        'password_save': "Gem adgangskode (krypteret)",
        'password_saved': "✓ Adgangskode for denne fil er gemt",
        'password_wrong': "Forkert adgangskode",
        'password_mismatch': "Adgangskoderne stemmer ikke overens",
        'password_too_short': "Adgangskode for kort",
        'password_min_length': "Adgangskoden skal være mindst 4 tegn lang",
        'password_strength': "Adgangskodestyrke",
        'password_strength_very_weak': "Meget svag",
        'password_strength_weak': "Svag",
        'password_strength_medium': "Middel",
        'password_strength_strong': "Stærk",
        'password_strength_very_strong': "Meget stærk",
        'password_char_count': "({0} tegn)",
        'password_match': "✓ Stemmer overens",
        'password_no_match': "✗ Adgangskoder stemmer ikke overens",
        'password_show': "Vis",
        'password_hide': "Skjul",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Adgangskodehåndtering",
        'password_table_filename': "Filnavn",
        'password_table_password': "Adgangskode",
        'password_count': "{0} gemt adgangskode{1}",
        'password_count_singular': "",
        'password_count_plural': "r",
        'password_none': "Ingen gemte adgangskoder",
        'password_copied': "{0} adgangskode{1} kopieret",
        'password_copied_singular': "",
        'password_copied_plural': "r",
        'password_delete_confirm': "Vil du virkelig slette adgangskoden for '{0}'?",
        'password_delete_multiple': "Vil du virkelig slette de {0} valgte adgangskoder?",
        'password_delete_all_confirm': "Vil du virkelig slette alle {0} gemte adgangskoder?",
        'password_deleted': "{0} adgangskode{1} slettet",
        'password_deleted_singular': "",
        'password_deleted_plural': "r",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Alle adgangskoder er slettet",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Adgangskodegenerator",
        'generator_generated': "Genereret adgangskode:",
        'generator_regenerate': "Generér igen",
        'generator_copy': "Kopiér",
        'generator_use': "Brug",
        'generator_settings': "Indstillinger",
        'generator_length': "Længde:",
        'generator_group_every': "Separator hver",
        'generator_group_chars': "tegn.   Separator:",
        'generator_uppercase': "Store bogstaver (A‑Z)",
        'generator_lowercase': "Små bogstaver (a‑z)",
        'generator_digits': "Tal (0‑9)",
        'generator_symbols': "Symboler (!@#$%^&*)",
        'generator_exclude': "Udelukket:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Master‑adgangskode påkrævet",
        'master_password_setup': "Opsæt master‑adgangskode",
        'master_password_change': "Skift master‑adgangskode",
        'master_password_enter': "Indtast din master‑adgangskode",
        'master_password_choose': "Vælg en stærk master‑adgangskode (mindst 8 tegn)",
        'master_password_new': "Indtast din nye master‑adgangskode",
        'master_password_confirm': "Bekræft adgangskode",
        'master_password_authenticate': "Godkend",
        'master_password_success': "Master‑adgangskode oprettet.",
        'master_password_changed': "Master‑adgangskode ændret.",
        'master_password_removed': "Master‑adgangskode og alle adgangskoder slettet.",
        'master_password_remove': "Fjern master‑adgangskode",
        'master_password_remove_confirm': "Er du SIKKER på, at du vil slette ALLE adgangskoder?\n\nDenne handling er UOPRETTELIG!",
        'master_password_export_before': "Vil du først eksportere en sikkerhedskopi?",
        'master_password_export_delete': "Eksportér og slet",
        'master_password_delete_now': "Slet nu",
        'master_password_for_signatures': "For at bruge underskrifter skal du oprette en master‑adgangskode.\n\nVil du oprette en master‑adgangskode nu?",
        'master_password_for_private': "For at bruge private tekstblokke skal du oprette en master‑adgangskode.\n\nVil du oprette en master‑adgangskode nu?",
        'master_password_info': """
            <b>🔐 UDEN MASTER‑ADGANGSKODE:</b><br>
            • Ingen visning, kopiering eller eksport af adgangskoder mulig<br>
            • Sletning af adgangskoder er altid mulig (også uden master‑adgangskode)<br><br>

            <b>🔐 MED MASTER‑ADGANGSKODE:</b><br>
            • Alle funktioner tilgængelige efter godkendelse<br>
            • Adgangskoder krypteres med master‑adgangskoden<br>
            • Minimumslængde: 8 tegn<br>
            • Sikker SHA‑256 hash‑lagring<br><br>

            <b>VIGTIGT:</b><br>
            • Hvis master‑adgangskoden mistes, kan adgangskoder ikke gendannes<br>
            • Når master‑adgangskoden fjernes, slettes ALLE adgangskoder<br>
            • Eksportmulighed før sletning<br>
            • Master‑adgangskoden kan altid ændres
        """,
        'signature_auth_disabled': "Deaktivér adgangskodeforespørgsel for underskrifter",
        'template_auth_disabled': "Deaktivér adgangskodeforespørgsel for private tekstblokke",
        'master_password_for_signatures_settings': "For at bruge underskrifter skal du oprette en master‑adgangskode.\n\nGå til Indstillinger – Adgangskodehåndtering",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Beskyt PDF",
        'protect_info': "Filen '{0}' vil blive beskyttet med en adgangskode.",
        'protect_instruction': "Indtast den ønskede adgangskode to gange for at beskytte dokumentet, eller brug adgangskodegeneratoren til højre for indtastningsfeltet.",
        'protect_success': "PDF blev beskyttet og gemt som:\n{0}\n\nAdgangskode: {1}\n\nVil du åbne den beskyttede PDF nu?",
        'protect_open': "Ja",
        'protect_skip': "Nej",
        'protect_error': "Fejl ved beskyttelse af PDF",
        'protect_open_title': "åbn beskyttet PDF",
        'protect_question': "Færdig. Vil du åbne den beskyttede PDF nu? Ja eller Nej?",
        'password_cancel': "Adgangskodedialog annulleret",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Slet sider",
        'pages_extract': "Uddrag sider",
        'pages_insert': "Indsæt sider",
        'pages_move': "Flyt sider",
        'pages_delete_options': "Sletningsmuligheder",
        'pages_delete_empty': "Slet alle tomme sider",
        'pages_delete_current': "Slet aktuel side",
        'pages_delete_range': "Slet sideinterval",
        'pages_extract_options': "Uddragelsesmuligheder",
        'pages_extract_current': "Uddrag aktuel side",
        'pages_extract_range': "Uddrag sideinterval",
        'pages_insert_position': "Indsættelsesposition",
        'pages_insert_before': "Indsæt før side:",
        'pages_insert_select': "Vælg PDF",
        'pages_insert_none': "Ingen PDF valgt",
        'pages_move_source': "Sider der skal flyttes",
        'pages_move_from': "Fra side:",
        'pages_move_to': "Til side:",
        'pages_move_target': "Målposition",
        'pages_move_before': "Flyt før side:",
        'pages_move_hint': "Bemærk: side 1 = begyndelse, {0} = slutning",
        'pages_range_invalid': "Startside skal være mindre end eller lig med slutside.",
        'pages_position_invalid': "Målposition må ikke være inden for det interval, der skal flyttes.",
        'pages_no_pdf_selected': "Der er ikke valgt nogen PDF.",
        'pages_deleted': "{0} sider blev slettet.",
        'pages_extracted': "Uddraget: {0}\nGemt som: {1}\nFilstørrelse: {2:.1f} KB",
        'pages_inserted': "{0} sider indsat",
        'pages_moved': "{0} sider blev flyttet.",
        'pages_deleted_none': "Ingen sider blev slettet.",
        'pages_delete_progress': "Sletter sider...",
        'pages_deleted_with_backup': "{0} sider blev slettet.\n\nBackup: {1}",
        'pages_deleted_voice': "En backup blev oprettet, og {0} sider blev slettet.",
        'info': "Info",
        'error_dialog_creation': "Dialog kunne ikke oprettes",
        'extract_page_single': "Uddrag side {0}",
        'extract_page_range': "Uddrag sider {0}‑{1}",
        'extract_success_voice': "Sider uddraget",
        'extract_error_format': "Fejl ved uddragelse: {0}",
        'pages_inserted_voice': "{0} sider indsat.",
        'insert_error_format': "Fejl ved indsættelse: {0}",
        'pages_move_progress': "Flytter sider...",
        'pages_moved_with_backup': "{0} sider blev flyttet.\n\nBackup: {1}",
        'move_success_title': "Flytning lykkedes",
        'pages_moved_voice': "{0} sider flyttet",
        'mark_removed': "Markering fjernet fra side {0}",
        'mark_empty': "Side {0} markeret som tom",
        'mark_export_removed': "Eksportmarkering fjernet fra side {0}",
        'mark_export': "Side {0} markeret til eksport",
        'no_empty_pages': "Ingen tomme sider markeret til sletning",
        'delete_empty_confirm': "Vil du slette alle {0} markerede tomme sider?",
        'delete_empty_confirm_voice': "Slet nu alle {0} markerede tomme sider? Ja eller Nej.",
        'empty_pages_deleted': "{0} tomme sider slettet",
        'no_export_pages': "Ingen sider markeret til eksport",
        'overwrite_title': "Overskriv eksisterende fil",
        'overwrite_question': "Filen\n\n{0}\n\neksisterer allerede.\nVil du overskrive den?",
        'overwrite_voice': "Overskriv eksisterende fil? Ja eller Nej.",
        'page_skipped': "Side {0} blev sprunget over",
        'export_complete': "Eksport færdig.",
        'export_complete_voice': "Eksporten er færdig.",
        'no_pages_exported': "Ingen side eksporteret",
        'export_cancelled': "Eksport annulleret",
        'pages_exported': "{0} sider eksporteret til {1}",
        'export_page_title': "Eksportér side",
        'page_exported': "Side {0} eksporteret til {1}",
        'export_error': "Fejl ved eksport",
        'export_marked_title': "Eksportér markerede sider",
        'rotate_all_title': "roter alle sider",
        'rotate_all_question': "Vil du rotere alle sider 90 grader til højre?",
        'rotate_all_voice': "Vil du rotere alle sider 90 grader til højre? Ja eller Nej?",
        'all_pages_rotated': "Alle sider roteret",
        'page_rotated': "Side {0} roteret",
        'rotate_error': "Siden kunne ikke roteres",
        'delete_page_confirm': "Vil du slette side {0}?",
        'delete_page_confirm_voice': "Vil du virkelig slette side {0}? Ja eller Nej.",
        'page_deleted': "Side {0} slettet",
        'delete_error': "Siden kunne ikke slettes",
        'pages_deleted_voice': "{0} sider slettet",
        'pages_exported_split': "{0} sider blev eksporteret.",
        'pages_skipped': "{0} sider blev sprunget over.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Uddrag sider (avanceret)",
        'pdf_splitter_title': "PDF‑splitter og ‑udtrækker",
        'pdf_splitter_load': " Vælg PDF‑fil",
        'pdf_splitter_info': "Vælg en mulighed for dit PDF‑dokument",
        'pdf_splitter_basic': "Grundlæggende handlinger",
        'pdf_splitter_single': "Del op i enkelte sider",
        'pdf_splitter_range': "Uddrag sider:",
        'pdf_splitter_range_placeholder': "f.eks. 1‑3,5,7‑9",
        'pdf_splitter_clean': "Oprydningshandlinger",
        'pdf_splitter_remove_empty': "Fjern alle tomme sider",
        'pdf_splitter_remove': "Slet sideinterval:",
        'pdf_splitter_remove_placeholder': "f.eks. 2,4‑6",
        'pdf_splitter_process': "Bearbejd PDF",
        'pdf_splitter_loaded': "PDF indlæst. Vælg en mulighed",
        'pdf_read_error': "PDF kunne ikke læses",
        'pages': "Sider",
        'pages_created': "Sider oprettet",
        'range_empty': "Indtast et sideinterval",
        'range_invalid': "Ugyldigt sideinterval",
        'range_created': "Ny PDF med de valgte sider oprettet:\n{0}",
        'empty_removed': "{0} tomme sider fjernet.\nOutput: {1}",
        'remove_empty': "Indtast sider, der skal fjernes",
        'remove_invalid': "Ugyldige sider at fjerne",
        'remove_done': "Oprenset PDF oprettet:\n{0}",
        'open_folder': "Åbn mappe",
        'show_in_finder': "Vis i Finder",
        'pdf_splitter_no_pdf': "Indlæs først en PDF‑fil.",
        'process_error': "Fejl ved bearbejdning af PDF",
        'pages_created_voice': "{0} sider oprettet",
        'range_created_voice': "PDF med de valgte sider oprettet",
        'empty_removed_voice': "{0} tomme sider fjernet",
        'remove_done_voice': "Oprenset PDF oprettet",
        'pdf_splitter_split_groups': "Hver sammenhængende gruppe i separat fil",
        'range_created_single': "Ny PDF oprettet:\n{0}",
        'range_created_multiple': "{0} PDF‑filer oprettet.",
        'range_created_voice_single': "En PDF med de valgte sider oprettet",
        'range_created_voice_multiple': "{0} PDF‑filer oprettet",
        'empty_removed_none_left': "Ingen sider tilbage",
        'empty_removed_all_empty': "Alle sider blev genkendt som tomme og ville blive fjernet. Ingen fil oprettet.",
        'preview_single': "Forhåndsvisning: {0}",
        'preview_enter_range': "Indtast et sideinterval.",
        'preview_invalid_range': "Ugyldigt sideinterval.",
        'preview_file': "Forhåndsvisning: {0}",
        'preview_files': "Forhåndsvisning: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Starter udskrivning",
        'print_sent': "Udskriftsjob sendt",
        'print_now': "Udskriv nu",
        'print_error': "Fejl ved direkte udskrivning",
        'print_limited': "Udskrivningsfunktion begrænset på dette system",
        'print_error_format': "Fejl ved direkte udskrivning: {0}",
        'warning': "Bemærkning",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Skift til lys tilstand",
        'mode_switch_to_dark': "Skift til mørk tilstand",
        'mode_dark_activated': "Mørk tilstand aktiveret",
        'mode_light_activated': "Lys tilstand aktiveret",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Fuld visning",
        'zoom_two_pages': "To sider side om side",
        'zoom_overview': "Oversigtstilstand",
        'zoom_cannot_during_search': "Zoom ikke muligt under søgning",
        'zoom_exit_first': "Forlad først zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Træk og slip aktiveret",
        'drag_disabled': "Træk og slip deaktiveret",
        'drag_page_grab': "Griber side {0}",
        'drag_page_dropped': "Side {0} indsat på position {1}",
        'drag_position_invalid': "Ugyldig position",
        'drag_same_position': "Side {0} forbliver på position {0}",
        'drag_error': "Fejl ved flytning",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Tekstindtastning med avanceret formatering og tekstblokhåndtering",
        'text_templates': "Tilgængelige tekstblokke:",
        'text_name': "Navn",
        'text_preview': "Teksteksempel",
        'text_enter': "Tekst:",
        'text_font_size': "Skriftstørrelse:",
        'text_formatting': "Formatering:",
        'text_bold': "Fed",
        'text_italic': "Kursiv",
        'text_underline': "Understreget",
        'text_alignment': "Justering:",
        'text_left': "Venstre",
        'text_center': "Centreret",
        'text_right': "Højre",
        'text_color': "Tekstfarve:",
        'text_opacity': "Gennemsigtighed:",
        'text_word_wrap': "Orddeling:",
        'text_auto': "Automatisk",
        'text_page_width_95': "Sidebredde (95%)",
        'text_page_width_85': "Meget bred (85%)",
        'text_page_width_75': "Bredere (75%)",
        'text_page_width_60': "Bred (60%)",
        'text_page_width_50': "Mellem (50%)",
        'text_page_width_30': "Smal (30%)",
        'text_page_width_20': "Smallere (20%)",
        'text_page_width_10': "Meget smal (10%)",
        'text_no_wrap': "Ingen ombrydning",
        'text_private': "Privat tekstblok (kræver godkendelse)",
        'text_preview_label': "Eksempel:",
        'text_preview_placeholder': "Her vises et eksempel på teksten...",
        'text_no_text': "(Ingen tekst)",
        'text_save_template': "💾 Gem som blok",
        'text_delete_template': "🗑 Slet valgt tekstblok",
        'text_show_private': "Vis private",
        'text_hide_private': "Skjul private",
        'text_use': "✅ Brug tekst",
        'text_saved': "Tekstblok gemt som:\n{0}",
        'text_saved_voice': "Tekstblok gemt",
        'text_deleted': "Tekstblok slettet",
        'text_no_text_to_save': "Ingen tekst at gemme.",
        'text_no_templates': "Ingen tekstblokke fundet",
        'text_private_master_required': "Private blokke kan kun bruges, hvis en master‑adgangskode er oprettet.\n\nVil du oprette en master‑adgangskode nu?",
        'text_filename': "Filnavn til tekstblok (uden 'Text_' og '.txt'):",
        'text_filename_hint': "Eksempel: 'Telefon Hjem' gemmes som 'Text_Telefon Hjem.txt'",
        'text_save_hint': "Tekstblokken gemmes automatisk med formatering.",
        'text_guide_title': "Tekstindtastning - Vejledning",
        'text_delete_confirm': "Vil du virkelig slette tekstblokken?\n\nFil: {0}\nTekst: {1}...",
        'text_make_public': "Markér som offentlig",
        'text_make_private': "Markér som privat",
        'text_privacy_changed': "Privatstatus ændret",
        'text_private_always': "Private altid synlige (indstilling)",
        'text_mode_required': "Aktivér først teksttilstand",
        'text_continue_editing': "Fortsæt redigering – markør i slutningen af teksten",
        'text_no_input': "Ingen tekst indtastet – tekst kasseret",
        'save_dialog_question': "Hvordan vil du fortsætte?",
        'text_save_question': "Gem alle tekster og krydser, justér, fortsæt redigering eller kassér?",
        'copy_cross': "Kryds kopieret",
        'paste_cross': "Kryds indsat",
        'paste_text': "Tekst indsat",
        'cross_discarded': "Kryds kasseret",
        'all_discarded': "Alt kasseret",
        'text_discarded': "Tekst kasseret",
        'no_texts_to_save': "Ingen tekster at gemme",
        'no_valid_texts': "Ingen gyldige tekster at gemme",
        'text_word_singular': "tekst",
        'text_word_plural': "tekster",
        'cross_word_singular': "kryds",
        'cross_word_plural': "krydser",
        'texts_saved_title': "Tekster gemt",
        'texts_crosses_saved': "{0} {1} og {2} {3} blev indsat i PDF'en.\n\nPDF genindlæst...",
        'texts_crosses_saved_voice': "{0} {1} og {2} {3} gemt.",
        'texts_saved': "{0} {1} blev indsat i PDF'en.\n\nPDF genindlæst...",
        'texts_saved_voice': "{0} {1} gemt.",
        'crosses_saved': "{0} {1} blev indsat i PDF'en.\n\nPDF genindlæst...",
        'crosses_saved_voice': "{0} {1} gemt.",
        'elements_saved': "{0} elementer blev indsat i PDF'en.\n\nPDF genindlæst...",
        'elements_saved_voice': "{0} elementer gemt.",
        'text_window_load_error': "Tekstvindue kunne ikke indlæses",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Tekstindtastning og tekstblokke – Detaljeret vejledning**

        **1. Indsæt og rediger tekst**
        - Højreklik på det ønskede sted i dokumentet, og vælg "Indsæt tekst".
        - Der åbnes en dialog, hvor du kan indtaste og formatere din tekst:
        • Skriftstørrelse, Fed, Kursiv, Understreget
        • Tekstfarve (frit valg)
        • Gennemsigtighed via skydekontakt
        • Orddeling (forskellige bredder, f.eks. sidebredde, smal, ingen ombrydning)
        - Efter bekræftelse vises teksten på klikpositionen. Du kan flytte den med musen eller piletasterne.
        - Dobbeltklik på teksten åbner redigeringstilstand; ESC forlader den.

        **2. Administrer tekstblokke (skabeloner)**
        - I tekstdialogen ser du til venstre en liste over alle gemte tekstblokke.
        - **Gem en blok:** Indtast din tekst, formater den, og klik på "💾 Gem som blok". Indtast et filnavn (uden endelse).
        - **Indlæs en blok:** Klik på det ønskede navn i listen. Teksten og formateringen overtages og kan justeres efter behov.
        - **Slet:** Højreklik på en blok for at slette den eller ændre dens privatstatus.

        **3. Private tekstblokke (master‑adgangskode)**
        - Hvis du har oprettet en master‑adgangskode (under Indstillinger → Adgangskodehåndtering), kan du markere blokke som "private".
        - Aktiver afkrydsningsfeltet "Privat tekstblok" i dialogen, før du gemmer.
        - Private blokke vises kun i listen, når du én gang pr. session har indtastet din master‑adgangskode (godkendelse via låsesymbolet eller ved første adgang).
        - På den måde beskytter du fortrolige tekstblokke mod uautoriseret adgang.

        **4. Indsæt krydser**
        - Via kontekstmenuen kan du også indsætte et grafisk kryds (f.eks. til afkrydsningsfelter).
        - Størrelsen, stregtykkelsen og farven på krydser kan justeres globalt i indstillingerne (menu "Indstillinger" → "Krydsindstillinger").
        - Højreklik på et eksisterende kryds for at ændre det individuelt.

        **5. Samlehandlinger**
        - Hvis du har placeret flere tekster eller krydser på en side, kan du gemme eller kassere alle elementer på én gang via kontekstmenuen (højreklik i teksttilstand).
        - Ved lagring indlejres alle elementer i PDF'en og forbliver som vektorgrafik.

        **6. Tastaturgenveje i teksttilstand**
        - Piletaster: flyt element
        - Ctrl+Piletaster: større skridt
        - Enter: åbn gem‑dialog (gem alt / justér / kassér)
        - ESC: kassér aktuelt element
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Tekstindtastning og tekstblokke – Detaljeret vejledning</strong></p>

        <p><strong>1. Indsæt og rediger tekst</strong></p>
        <ul>
        <li>Højreklik på det ønskede sted i dokumentet, og vælg "Indsæt tekst".</li>
        <li>Der åbnes en dialog, hvor du kan indtaste og formatere din tekst:<br/>
        • Skriftstørrelse, Fed, Kursiv, Understreget<br/>
        • Tekstfarve (frit valg)<br/>
        • Gennemsigtighed via skydekontakt<br/>
        • Orddeling (forskellige bredder, f.eks. sidebredde, smal, ingen ombrydning)</li>
        <li>Efter bekræftelse vises teksten på klikpositionen. Du kan flytte den med musen eller piletasterne.</li>
        <li>Dobbeltklik på teksten åbner redigeringstilstand; ESC forlader den.</li>
        </ul>

        <p><strong>2. Administrer tekstblokke (skabeloner)</strong></p>
        <ul>
        <li>I tekstdialogen ser du til venstre en liste over alle gemte tekstblokke.</li>
        <li><strong>Gem en blok:</strong> Indtast din tekst, formater den, og klik på "💾 Gem som blok". Indtast et filnavn (uden endelse).</li>
        <li><strong>Indlæs en blok:</strong> Klik på det ønskede navn i listen. Teksten og formateringen overtages og kan justeres efter behov.</li>
        <li><strong>Slet:</strong> Højreklik på en blok for at slette den eller ændre dens privatstatus.</li>
        </ul>

        <p><strong>3. Private tekstblokke (master‑adgangskode)</strong></p>
        <ul>
        <li>Hvis du har oprettet en master‑adgangskode (under Indstillinger → Adgangskodehåndtering), kan du markere blokke som "private".</li>
        <li>Aktiver afkrydsningsfeltet "Privat tekstblok" i dialogen, før du gemmer.</li>
        <li>Private blokke vises kun i listen, når du én gang pr. session har indtastet din master‑adgangskode (godkendelse via låsesymbolet eller ved første adgang).</li>
        <li>På den måde beskytter du fortrolige tekstblokke mod uautoriseret adgang.</li>
        </ul>

        <p><strong>4. Indsæt krydser</strong></p>
        <ul>
        <li>Via kontekstmenuen kan du også indsætte et grafisk kryds (f.eks. til afkrydsningsfelter).</li>
        <li>Størrelsen, stregtykkelsen og farven på krydser kan justeres globalt i indstillingerne (menu "Indstillinger" → "Krydsindstillinger").</li>
        <li>Højreklik på et eksisterende kryds for at ændre det individuelt.</li>
        </ul>

        <p><strong>5. Samlehandlinger</strong></p>
        <ul>
        <li>Hvis du har placeret flere tekster eller krydser på en side, kan du gemme eller kassere alle elementer på én gang via kontekstmenuen (højreklik i teksttilstand).</li>
        <li>Ved lagring indlejres alle elementer i PDF'en og forbliver som vektorgrafik.</li>
        </ul>

        <p><strong>6. Tastaturgenveje i teksttilstand</strong></p>
        <ul>
        <li>Piletaster: flyt element</li>
        <li>Ctrl+Piletaster: større skridt</li>
        <li>Enter: åbn gem‑dialog (gem alt / justér / kassér)</li>
        <li>ESC: kassér aktuelt element</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Krydsindstillinger",
        'cross_properties': "Krydsegenskaber",
        'cross_size': "Størrelse (px):",
        'cross_line_width': "Stregtykkelse:",
        'cross_color': "Farve:",
        'cross_choose_color': "Vælg",
        'cross_fine_tuning': "Finjustering ved lagring (pixels)",
        'cross_offset_x': "X‑forskydning:",
        'cross_offset_y': "Y‑forskydning:",
        'cross_offset_x_tooltip': "Negative værdier flytter krydset til venstre ved lagring, positive til højre",
        'cross_offset_y_tooltip': "Negative værdier flytter krydset opad ved lagring, positive nedad",
        'cross_preview': "Eksempel",
        'cross_save': "Anvend indstillinger",
        'cross_customized': "Kryds tilpasset",
        'cross_settings_applied': "Krydsindstillinger gemt.\nStørrelse: {0}px, Stregtykkelse: {1}px\n{2}",
        'cross_updated_count': "{0} eksisterende krydser blev opdateret.",
        'cross_no_crosses': "Ingen eksisterende krydser fundet.",
        'cross_settings_applied_all': "Krydsindstillinger anvendt på alle {0} krydser",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Underskriftsindstillinger",
        'signature_1': "Underskrift 1",
        'signature_2': "Underskrift 2",
        'signature_select': "Vælg underskrift",
        'signature_add': "➕ Tilføj ny underskrift...",
        'signature_size': "Størrelse for underskrift {0} (%):",
        'signature_common': "Generelle indstillinger",
        'signature_timestamp': "Tilføj automatisk tidsstempel",
        'signature_location': "Standardsted:",
        'signature_timestamp_size': "Skriftstørrelse for tidsstempel:",
        'signature_no_files': "-- Ingen underskrifter fundet --",
        'signature_insert': "Indsæt underskrift",
        'signature_insert_1': "Indsæt underskrift 1",
        'signature_insert_2': "Indsæt underskrift 2",
        'signature_customize': " Tilpas underskrift",
        'signature_discard': " Kassér denne underskrift",
        'signature_save_all': " Gem alle underskrifter",
        'signature_discard_all': " Kassér alle underskrifter",
        'signature_guide_title': "Underskrifter - Vejledning",
        'signature_guide': """
📝 Underskrifter - Hurtigvejledning

- Opret master‑adgangskode
- Konfigurér underskrifter i menuen Indstillinger
  (størrelse, tidsstempel ...)
- Indsæt med HØJREKLIK på det ønskede sted
  (master‑adgangskode kræves én gang pr. session)
- Flyt underskriften med musen eller piletasterne
- Flere underskrifter kan indsættes efter hinanden
- Hver underskrift kan tilpasses individuelt
- Kassér en enkelt underskrift
- Gem / kassér alle underskrifter på én gang
- Alternativt kan menulinjen bruges.
        """,
        'signature_placeholder': "Intet eksempel tilgængeligt",
        'signature_info': "Underskrift {0}: {1}×{2} px ({3}% af {4}×{5})",
        'signature_info_placeholder': "Indstillinger for underskrift {0}",
        'signature_inserted': "Underskrift {0} indsat på side {1}",
        'signature_deleted': "Underskrift slettet",
        'signature_copied': "Underskrift kopieret",
        'signature_pasted': "Underskrift {0} indsat",
        'signature_saved': "{0} underskrifter blev indsat i PDF'en.\n\nPDF genindlæst...",
        'signature_saved_voice': "{0} underskrifter gemt",
        'mode_replace_signature_format': "Afslut tilstand og indsæt underskrift {0}",
        'mode_conflict_voice_signature': "{0}‑tilstand er aktiv. Afslut og indsæt underskrift?",
        'signature_not_configured': "Underskrift {0} ikke konfigureret",
        'signature_file_not_found': "Underskriftsfil ikke fundet",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Ingen kopieret underskrift tilgængelig",
        'no_signatures_to_save': "Ingen underskrifter at gemme",
        'signature_save_question': "Gem alle underskrifter, justér eller kassér denne?",
        'signatures_saved_title': "Underskrifter gemt",
        'signatures_saved': "{0} underskrifter blev indsat i PDF'en.\n\nPDF genindlæst...",
        'signatures_saved_voice': "{0} underskrifter gemt.",
        'all_signatures_discarded': "Alle underskrifter kasseret",
        'signature_settings_saved': "Underskriftsindstillinger gemt",
        'signature_cancelled': "Underskrift kasseret",
        'signature_active_title': "Underskrift aktiv",
        'signature_replace_question': "Der er allerede en aktiv underskrift.\n\nVil du erstatte den aktuelle underskrift?",
        'signature_replace': "Erstat underskrift",
        'signature_replace_voice': "Erstat aktuel underskrift eller annuller?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Billedindstillinger",
        'image_common': "Generelle billedindstillinger",
        'image_keep_aspect': "Bevar størrelsesforhold ved træk",
        'image_default_size': "Standardstørrelse (%):",
        'image_dark_invert': "Invertér billeder i mørk tilstand",
        'image_dark_invert_tooltip': "Aktiveret: billeder inverteres for bedre synlighed",
        'image_fine_tuning': "Finjustering (pixels)",
        'image_offset_x': "X‑forskydning:",
        'image_offset_y': "Y‑forskydning:",
        'image_offset_x_tooltip': "Negative værdier flytter billedet til venstre ved lagring, positive til højre",
        'image_offset_y_tooltip': "Negative værdier flytter billedet opad ved lagring, positive nedad",
        'image_select': "Vælg billede",
        'image_insert': "Indsæt billede",
        'image_customize': " Tilpas billede",
        'image_aspect': " Bevar størrelsesforhold",
        'image_discard': " Kassér dette billede",
        'image_save_all': " Gem alle billeder",
        'image_discard_all': " Kassér alle billeder",
        'image_filter': "Billeder",
        'image_guide_title': "Indsæt billede - Vejledning",
        'image_guide': """
📷 Indsæt billede i PDF - Hurtigvejledning:

1. Højreklik på det ønskede sted
2. "Indsæt billede" → vælg billede
3. Placer billedet: træk med musen
4. Justér størrelsen: træk i hjørner/kanter
5. Bevar størrelsesforhold: [A]‑tast
6. Yderligere justeringer: højreklik på billede

Tip: Du kan justere indstillingerne i kontekstmenuen.
        """,
        'image_inserted': "Billede {0} indsat på side {1}",
        'image_deleted': "Billede kasseret",
        'image_copied': "Billede kopieret",
        'image_pasted': "Billede indsat",
        'image_saved': "{0} billeder blev indsat i PDF'en.\n\nPDF genindlæst...",
        'image_saved_voice': "{0} billeder gemt",
        'image_aspect_on': "aktiveret",
        'image_aspect_off': "deaktiveret",
        'image_aspect_toggle': "Bevar størrelsesforhold {0}",
        'image_reset': "Billede nulstillet til original størrelse",
        'image_replaced': "Billede erstattet",
        'image_invalid': "Ikke et gyldigt billede",
        'mode_replace_image': "Indsæt billede",
        'mode_conflict_voice_image': "{0}‑tilstand er aktiv. Afslut og indsæt billede?",
        'image_active_title': "Billede aktivt",
        'image_replace_question': "Der er allerede et aktivt billede.\n\nVil du erstatte det aktuelle billede?",
        'image_replace': "Erstat billede",
        'image_replace_voice': "Erstat aktuelt billede eller annuller?",
        'image_filter_all': "Billeder (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Alle filer (*.*)",
        'no_copied_image': "Intet kopieret billede tilgængeligt",
        'image_discarded': "Billede kasseret",
        'image_save_question': "Gem alle billeder, justér eller kassér dette?",
        'no_images_to_save': "Ingen billeder at gemme",
        'no_valid_images': "Ingen gyldige billeder at gemme",
        'images_saved_title': "Billeder gemt",
        'images_saved': "{0} billeder blev indsat i PDF'en.\n\nPDF genindlæst...",
        'images_saved_voice': "{0} billeder gemt.",
        'all_images_discarded': "Alle billeder kasseret",
        'image_settings_updated': "Billedindstillinger opdateret",
        'image_replace_title': "Vælg nyt billede",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Formindstillinger",
        'form_basic': "Grundlæggende indstillinger",
        'form_default_type': "Standardformtype:",
        'form_rectangle': "Rektangel",
        'form_ellipse': "Ellipse",
        'form_line': "Linje",
        'form_arrow': "Pil",
        'form_line_width': "Stregtykkelse:",
        'form_colors': "Farver",
        'form_line_color': "Linjefarve:",
        'form_fill_color': "Fyldfarve:",
        'form_choose_color': "Vælg",
        'form_transparent': "Gennemsigtig baggrund (kun linje)",
        'form_filled': "udfyldt",
        'form_dark_mode': "Mørk tilstand",
        'form_dark_invert': "Invertér farver i mørk tilstand",
        'form_fine_tuning': "Finjustering (pixels)",
        'form_offset_x': "X‑forskydning:",
        'form_offset_y': "Y‑forskydning:",
        'form_offset_x_tooltip': "Negative værdier flytter formen til venstre ved lagring, positive til højre",
        'form_offset_y_tooltip': "Negative værdier flytter formen opad ved lagring, positive nedad",
        'form_preview': "Eksempel",
        'form_insert': "Indsæt form",
        'form_rectangle_insert': "Rektangel",
        'form_ellipse_insert': "Ellipse/Cirkel",
        'form_line_insert': "Linje (2 klik)",
        'form_arrow_insert': "Pil (2 klik)",
        'form_customize': " Tilpas form",
        'form_transparent_toggle': " Gennemsigtig baggrund",
        'form_discard': " Kassér denne form",
        'form_save_all': " Gem alle former",
        'form_discard_all': " Kassér alle former",
        'form_guide_title': "Indsæt form - Vejledning",
        'form_guide': """
📐 Indsæt form i PDF - Hurtigvejledning:

1. Vælg formtype (rektangel, ellipse, linje, pil)
2. Klik på positionen
   - For rektangel/ellipse: ét klik placerer formen
   - For linje/pil: to klik for start‑ og slutpunkt
3. Placer formen: træk med musen
4. Justér størrelsen: træk i hjørner/kanter
5. Gem formen: Enter
6. Kassér formen: ESC
7. Yderligere justeringer: højreklik på form

Tip: Du kan justere indstillingerne i kontekstmenuen.
        """,
        'form_inserted': "{0} indsat på side {1}",
        'form_deleted': "Form slettet",
        'form_copied': "Form kopieret",
        'form_pasted': "Form indsat",
        'form_saved': "{0} former blev indsat i PDF'en.\n\nPDF genindlæst...",
        'form_saved_voice': "{0} former gemt",
        'form_reset': "Form nulstillet til standardstørrelse",
        'form_transparent_on': "aktiveret",
        'form_transparent_off': "deaktiveret",
        'form_transparent_toggled': "Gennemsigtig baggrund {0}",
        'form_line_cancel': "Linjetegning annulleret",
        'form_second_click': "Klik nu på slutpunktet for {0}",
        'mode_replace_form': "Indsæt form",
        'mode_conflict_voice_form': "{0}‑tilstand er aktiv. Afslut og indsæt en form?",
        'form_settings_updated': "Formindstillinger opdateret",
        'form_unknown': "Form",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klik på startpositionen",
        'form_line_guide_2': "2. Klik på slutpositionen",
        'form_line_guide_3': "Linjen vil blive tegnet mellem de to punkter.",
        'form_line_status_1': "Venter på første klik...",
        'form_line_status_2': "Første punkt angivet: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Klik nu på slutpunktet...",
        'form_line_status_4': "Begge punkter angivet.\nKlik på 'Færdig' for at gemme.",
        'form_line_reset': "Nulstil",
        'form_line_finish': "Færdig",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopiér (Cmd+C)",
        'paste': "Indsæt (Cmd+V)",
        'copied': "Kopieret: {0}",
        'no_element_to_copy': "Intet element valgt til kopiering",
        'no_copied_data': "Ingen kopierede data tilgængelige",
        'no_valid_position': "Ingen gyldig position at indsætte på",
        'copy_text': "Tekst kopieret",
        'copy_image': "Billede kopieret",
        'copy_form': "Form kopieret",
        'copy_signature': "Underskrift kopieret",
        'element_text': "tekst",
        'element_image': "billede",
        'element_form': "form",
        'element_signature': "underskrift",
        'element_unknown': "element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Tilstandskonflikt",
        'mode_conflict_message': "Tilstanden '{0}' er allerede aktiv.\n\nVil du afslutte den og {1}?",
        'mode_replace': "Afslut tilstand og {0}",
        'mode_cancel': "Annuller",
        'mode_replace_text': "indsæt tekst",
        'mode_replace_cross': "indsæt kryds",
        'mode_replace_signature': "indsæt underskrift",
        'mode_replace_image': "indsæt billede",
        'mode_replace_form': "indsæt form",
        'mode_conflict_voice': "{0}‑tilstand er aktiv. Afslut og indsæt tekst?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Tekstindtastning",
        'active_mode_signature': "Underskrift",
        'active_mode_image': "Billede",
        'active_mode_form': "Form",
        'active_mode_and': " og ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Indsæt",                    # Hauptmenü
        'insert_another_text': "Indsæt tekst",          # Vereinfacht
        'insert_another_cross': "Indsæt kryds",        # Vereinfacht
        'insert_another_signature_1': "Underskrift 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Underskrift 2",      # Untermenü-Eintrag
        'insert_another_image': "Indsæt billede",         # Vereinfacht
        'insert_another_form_rect': "Rektangel",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Ellipse",        # Untermenü-Eintrag
        'insert_another_form_line': "Linje (2 klik)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Pil (2 klik)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Gem {0}",
        'save_dialog_message': "{0} vil blive gemt på side {1}.\n\nHvordan vil du fortsætte?",
        'save_all': "Gem alle {0}",
        'save_single': "Gem {0}",
        'save_customize': "Justér {0}",
        'save_discard': "Kassér {0}",
        'save_continue': "Fortsæt redigering",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Gå til side {0}",
        'context_rotate': " Roter side {0}",
        'context_delete': " Slet side {0}",
        'context_export': " Eksportér side {0}",
        'context_mark_as': " Markér side som...",
        'context_mark_empty': " Tom side",
        'context_unmark_empty': " Ikke længere tom",
        'context_mark_export': " Markér til eksport",
        'context_unmark_export': " Eksportér ikke",
        'context_batch_actions': " Samlehandlinger",
        'context_batch_delete_empty': " Slet alle {0} tomme sider",
        'context_batch_export_single': " Alle {0} sider (én fil)",
        'context_batch_export_split': " Alle {0} sider (separate)",
        'context_drag_start': " Start træk og slip",
        'context_drag_stop': " Stop træk og slip",
        'context_insert': " Indsæt",
        'context_insert_pages': " Indsæt sider",
        'context_zoom': "Zoom",
        'discard_mixed': "Kassér {0} {1} og {2} {3}",
        'save_mixed': "Gem {0} {1} og {2} {3}",
        'discard_texts': "Kassér {0} tekster",
        'discard_text_single': "Kassér 1 tekst",
        'save_texts': "Gem {0} tekster",
        'save_text_single': "Gem 1 tekst",
        'discard_crosses': "Kassér {0} krydser",
        'discard_cross_single': "Kassér 1 kryds",
        'save_crosses': "Gem {0} krydser",
        'save_cross_single': "Gem 1 kryds",
        'discard_signatures': "Kassér {0} underskrifter",
        'save_signature_single': "Gem 1 underskrift",
        'save_signatures': "Gem {0} underskrifter",
        'discard_images': "Kassér {0} billeder",
        'save_image_single': "Gem 1 billede",
        'save_images': "Gem {0} billeder",
        'discard_forms': "Kassér {0} former",
        'save_form_single': "Gem 1 form",
        'save_forms': "Gem {0} former",
        'cross_discard': "Kassér dette kryds",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Eksport‑ / importinformation",
        'export_what': "📋 Hvad eksporteres?",
        'export_general': "Generelle indstillinger",
        'export_general_items': "• Taleoutput (til/fra, hastighed)\n• Mørk/lys tilstand\n• Backup‑indstillinger\n• OCR‑indstillinger",
        'export_image_form': "Billed‑ og formindstillinger",
        'export_image_form_items': "• Billedindstillinger (størrelsesforhold, standardstørrelse)\n• Formindstillinger (stregtykkelse, farver)\n• Underskriftsindstillinger (stier, størrelser, tidsstempel)",
        'export_passwords': "Adgangskodedatabase",
        'export_passwords_items': "• Alle gemte PDF‑adgangskoder\n• Valgfrit krypteret eller dekrypteret",
        'export_master': "Master‑adgangskodeindstillinger",
        'export_master_items': "• Master‑adgangskode‑hash\n• Indstillinger for underskrifter/tekstblokke",
        'export_signatures': "Underskrifter og tekstblokke",
        'export_signatures_items': "• Alle billedfiler (underskrifter)\n• Alle tekstblokke med formatering\n• Private/offentlige markeringer",
        'export_import_warning': "⚠️ Vigtige bemærkninger",
        'export_import_note': "• Ved import overskrives ALLE nuværende indstillinger\n• Genstart af applikationen er nødvendig\n• Eksisterende underskrifter/tekstblokke erstattes",
        'export_master_note': "• Hvis en master‑adgangskode er angivet, kan du vælge:\n  - Dekrypteret (adgangskoder i klartekst)\n  - Krypteret (kun læsbar med master‑adgangskode)",
        'export_security': "• Den eksporterede ZIP‑fil indeholder fortrolige data\n• Opbevar den sikkert (f.eks. krypteret USB‑stick)\n• Hvis filen mistes, er adgangskoder uigenkaldeligt tabt",
        'export_format': "📁 Eksportformat",
        'export_format_desc': "Indstillingerne gemmes i én enkelt ZIP‑fil:",
        'export_filename': "PDFDarkView_Indstillinger_ÅÅÅÅMMDD_TTMMSS.zip",
        'export_success': "Indstillinger eksporteret",
        'export_failed': "Eksport mislykkedes",
        'export_import_question': "Vil du genstarte applikationen nu?",
        'export_password_question': "Der er angivet en master‑adgangskode.\n\nVil du eksportere adgangskoderne dekrypteret?\n(ellers eksporteres de krypteret)",
        'export_decrypt': "Eksportér dekrypteret",
        'export_encrypt': "Eksportér krypteret",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Info",
        'info_title': "Om PDF Dark View",
        'info_version': "Version",
        'info_author': "Udviklet af Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Om",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> er en tilgængelig PDF-fremviser, der er specielt udviklet til personer med synshandicap.</p>

            <p><strong>Kernefunktioner:</strong></p>
            <ul>
                <li>Kontrastrig, tilpasselig brugergrænseflade</li>
                <li>Fuld tastaturstyring</li>
                <li>Integreret taleoutput</li>
                <li>OCR til scannede dokumenter</li>
                <li>Omfattende redigeringsværktøjer</li>
            </ul>

            <p>Mere end 50 sprog understøttes – så PDF'er er tilgængelige for alle.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funktioner",
        'info_features_intro': "PDF Dark View tilbyder dig følgende muligheder:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Visning & Navigation</strong> – Mørk/lys tilstand, sidevisning, zoom, spring til side</li>
            <li><strong>OCR (tekstgenkendelse)</strong> – Gør scannede dokumenter søgbare og kopierbare</li>
            <li><strong>Redigering</strong> – Indsæt tekst, krydser, signaturer, billeder og former</li>
            <li><strong>Sidehåndtering</strong> – Slet, ekstraher, indsæt, flyt via træk & slip</li>
            <li><strong>Eksport</strong> – Til Word, Pages eller som tekst</li>
            <li><strong>Sikkerhed</strong> – Adgangskodebeskyttelse og -styring</li>
            <li><strong>Tilgængelighed</strong> – Taleoutput, tastaturstyring, høj kontrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Betjening",
        'info_accessibility': "♿ Tilgængelighed – fuld tastaturstyring",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Generelt</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Åbn PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Søg</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Skift mellem mørk/lys tilstand</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Udskriv</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Afslut</div>

        <div class="shortcut-cat">📖 Navigation</div>
        <div class="shortcut-row"><kbd>Piletaster</kbd> Vend side for side</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Gå til side</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Første side</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Sidste side</div>

        <div class="shortcut-cat">✏️ Redigering</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Indsæt tekst</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Slet sider</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Ekstraher sider</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Indsæt sider</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Flyt sider</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Roter side</div>

        <div class="shortcut-cat">🖼️ Flyt elementer</div>
        <div class="shortcut-row"><kbd>Piletaster</kbd> Flyt tekst/billede/signatur</div>
        <div class="shortcut-row"><kbd>Ctrl+Piletaster</kbd> Større trin</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Gem</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Forkast</div>

        <div class="shortcut-cat">🗣️ Taleoutput</div>
        <div class="shortcut-row"><kbd>F2</kbd> Slå taleoutput til/fra</div>
        """,
        'info_contextmenu': "📌 Vigtigt: Alle funktioner er også tilgængelige via kontekstmenuen (højre museknap)!",
        'info_accessibility_hint': "💡 Tip: Taleoutput (F2) letter orienteringen og giver feedback om menuer og dialogbokse.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licens & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Oplysninger i henhold til § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Tyskland<br>
        E-mail: binhdiez64@gmail.com<br>
        Ansvarlig for indholdet: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Ansvarsfraskrivelse</strong><br>
        Softwaren er udviklet med største omhu. Der påtages intet ansvar for rigtigheden, fuldstændigheden og funktionaliteten. Brugen sker på egen risiko.<br><br>

        <strong>📄 MIT-licens (privat brug)</strong><br>
        Ophavsret (c) 2026 Toralf Schulz (BinhDiez)<br>
        Tilladt: gratis brug, private ændringer, personlige kopier.<br>
        Ikke tilladt: salg, kommerciel brug, fjernelse af ophavsretsmeddelelser.<br><br>

        <strong>🔧 Tredjepartskomponenter</strong><br>
        Denne software indeholder komponenter under GPL, AGPL, Apache 2.0, BSD og MIT-licenser.<br>
        Ved videredistribution skal de respektive licensbetingelser overholdes.<br><br>

        <strong>🌐 Open Source</strong><br>
        Kildekoden er tilgængelig og kan ses, ændres og videredistribueres i overensstemmelse med de respektive licensbetingelser.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Tak til",
        'info_credits': "Tak til open source-fællesskabet",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF-behandling</li>
            <li><strong>PyQt5</strong> – Grafisk brugergrænseflade</li>
            <li><strong>Tesseract OCR</strong> – Tekstgenkendelse</li>
            <li><strong>OCRmyPDF</strong> – OCR-integration</li>
            <li><strong>python-docx</strong> – Word-eksport</li>
            <li><strong>qtawesome</strong> – Ikoner</li>
            <li><strong>DeepSeek</strong> – Støtte til oversættelser (50+ sprog)</li>
            <li><strong>Alle brugere</strong> – For værdifuld feedback</li>
            <li><strong>Open source-fællesskabet</strong> – For fantastiske biblioteker</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Sprog",
        'info_languages_header': "🌍 Sprogunderstøttelse",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View understøtter i øjeblikket <strong>62 sprog</strong> – så softwaren kan bruges tilgængeligt over hele verden.</p>

            <p><strong>📖 Fuldstændig sprogliste (Status: Marts 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albansk (Shqip)</li>
                    <li>🇩🇿 Arabisk (العربية)</li>
                    <li>🇮🇩 Balinesisk (Basa Bali)</li>
                    <li>🇧🇩 Bengalsk (বাংলা)</li>
                    <li>🇲🇲 Burmesisk (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnisk (Bosanski)</li>
                    <li>🇧🇬 Bulgarsk (Български)</li>
                    <li>🇨🇳 Kinesisk (中文)</li>
                    <li>🇩🇰 Dansk (Dansk)</li>
                    <li>🇩🇪 Tysk</li>
                    <li>🇬🇧 Engelsk (English)</li>
                    <li>🇪🇪 Estisk (Eesti)</li>
                    <li>🇫🇮 Finsk (Suomi)</li>
                    <li>🇫🇷 Fransk (Français)</li>
                    <li>🇬🇷 Græsk (Ελληνικά)</li>
                    <li>🇮🇱 Hebraisk (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Kroatisk (Hrvatski)</li>
                    <li>🇭🇺 Ungarsk (Magyar)</li>
                    <li>🇮🇩 Indonesisk (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irsk (Gaeilge)</li>
                    <li>🇮🇸 Islandsk (Íslenska)</li>
                    <li>🇮🇹 Italiensk (Italiano)</li>
                    <li>🇯🇵 Japansk (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Koreansk (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Lettisk (Latviešu)</li>
                    <li>🇱🇹 Litauisk (Lietuvių)</li>
                    <li>🇱🇺 Luxembourgsk (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malaysisk (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolsk (Монгол)</li>
                    <li>🇳🇵 Nepalesisk (नेपाली)</li>
                    <li>🇳🇱 Nederlandsk (Nederlands)</li>
                    <li>🇳🇴 Norsk (Norsk)</li>
                    <li>🇦🇫 Pashto (پښتو)</li>
                    <li>🇮🇷 Persisk (فارسی)</li>
                    <li>🇵🇱 Polsk (Polski)</li>
                    <li>🇵🇹 Portugisisk (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumænsk (Română)</li>
                    <li>🇷🇺 Russisk (Русский)</li>
                    <li>🇸🇪 Svensk (Svenska)</li>
                    <li>🇷🇸 Serbisk (Српски)</li>
                    <li>🇸🇰 Slovakisk (Slovenčina)</li>
                    <li>🇸🇮 Slovensk (Slovenščina)</li>
                    <li>🇪🇸 Spansk (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thai (ไทย)</li>
                    <li>🇨🇿 Tjekkisk (Čeština)</li>
                    <li>🇹🇷 Tyrkisk (Türkçe)</li>
                    <li>🇺🇦 Ukrainsk (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamesisk (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Jiddisch (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Tilføj egne sprog:</strong><br>
                Ønsker du et sprog, der ikke er inkluderet endnu? Placer blot din egen ordbogsfil (<code>sprache_xx.py</code>) ved siden af applikationen – softwaren genkender den automatisk. Hvis du er interesseret i en specifik oversættelse, er du velkommen til at kontakte mig.
            </div>

            <p><strong>🙏 Særlig tak:</strong> DeepSeek for støtten til oversættelse af alle ordbøger til 62 sprog.</p>

            <p>📧 Kontakt for oversættelser: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Fejl",
        'error_occurred': "Der opstod en fejl",
        'error_pdf_load': "Fejl ved indlæsning af PDF",
        'error_pdf_save': "Fejl ved lagring af PDF",
        'error_ocr': "Fejl under tekstgenkendelse",
        'error_no_pdf': "Ingen PDF indlæst",
        'error_page_not_found': "Side ikke fundet",
        'error_invalid_range': "Ugyldigt sideinterval",
        'error_file_not_found': "Fil ikke fundet",
        'error_permission': "Ingen tilladelse",
        'error_unknown': "Ukendt fejl",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Succes",
        'success_operation': "Handlingen lykkedes",
        'success_saved': "Gemt",
        'success_exported': "Eksporteret",
        'success_imported': "Importeret",
        'success_deleted': "Slettet",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Bekræftelse",
        'confirm_yes': "Ja",
        'confirm_no': "Nej",
        'confirm_ok': "OK",
        'confirm_cancel': "Annuller",
        'confirm_delete': "Slet",
        'confirm_overwrite': "Overskriv",
        'confirm_continue': "Fortsæt",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Indlæser PDF...",
        'progress_saving': "Gemmer PDF...",
        'progress_exporting': "Eksporterer PDF...",
        'progress_processing': "Behandler...",
        'progress_wait': "Vent venligst...",
        'progress_preparing': "Forbereder...",
        'progress_finalizing': "Afslutter...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Hvid",
        'color_black': "Sort",
        'color_red': "Rød",
        'color_green': "Grøn",
        'color_blue': "Blå",
        'color_yellow': "Gul",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Orange",
        'color_gray': "Grå",
        'color_custom': "Farvevælger",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Fil",
        'menu_edit': "&Redigér",
        'menu_view': "&Vis",
        'menu_tools': "&Værktøjer",
        'menu_settings': "&Indstillinger",
        'menu_help': "&Hjælp",
        'menu_language': "🌐 Sprog",
        'menu_guides': "&Vejledninger",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Åbn",
        'file_save_as': "&Gem som...",
        'file_protect': "&Beskyt dokument...",
        'file_export': "&Eksportér",
        'file_export_pages': "Eksportér som Pages",
        'file_export_word': "Eksportér som DOCX",
        'file_export_text': "Eksportér som TXT",
        'file_print_now': "&Udskriv nu",
        'file_print': "&Udskriv",
        'file_close': "&Luk",
        'file_quit': "&Afslut",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Søg",
        'edit_ocr': " Kør OCR",
        'edit_rotate': "&Rotér side",
        'edit_rotate_all': "&Rotér alle sider",
        'edit_delete_pages': "&Slet sider",
        'edit_extract_pages': "&Uddrag sider",
        'edit_insert_pages': "&Indsæt sider",
        'edit_move_pages': "&Flyt sider",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Indsæt tekst og krydser",
        'text_insert': " Indsæt tekst",
        'cross_insert': " Indsæt kryds",
        'text_customize': " Tilpas tekst",
        'cross_customize': " Tilpas dette kryds",
        'cross_customize_all': " Tilpas alle krydser",
        'text_discard': " Kassér denne tekst/dette kryds",
        'text_discard_all': " Kassér alle tekster og krydser",
        'text_save_all': " Gem alle tekster og krydser",
        'text_guide': " Tekstindtastning / tekstblokke - Vejledning",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Indsæt underskrift",
        'signature_settings_menu': " Indstillinger...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Indsæt billede",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Indsæt former",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Vis tekstvindue",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Sidebredde (standard)",
        'view_zoom_two': "&To sider",
        'view_zoom_overview': "&Oversigt (flere sider)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Tilgængelighed",
        'settings_voice': "Taleoutput",
        'settings_voice_tooltip': "supplerer skærmlæseres taleoutput med ekstra information",
        'settings_signature': "&Underskriftsindstillinger",
        'settings_password': "&Adgangskodehåndtering",
        'settings_backup': "Opret backup før ændringer",
        'settings_export_import': "&Eksportér / importér indstillinger",
        'settings_export': "&Eksportér alle indstillinger...",
        'settings_import': "&Importér alle indstillinger...",
        'settings_export_info': "&Hvad eksporteres?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "til",
        'voice_off': "fra",
        'voice_toggle': "Taleoutput {0}",
        'voice_speed': "Hastighed {0} procent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Værktøj ikke fundet:\n{0}\n\nBASE_DIR: {1}\nSørg for, at PDF‑værktøjerne er installeret i mappen {1}.",
        'tool_started': "{0} startet",
        'tool_start_failed': "Kunne ikke starte",
        'process_error_failed_to_start': "Processen kunne ikke startes. Findes filen?",
        'process_error_crashed': "Processen gik ned under opstart.",
        'process_error_timeout': "Proces‑timeout nået.",
        'process_error_write': "Skrivefejl til processen.",
        'process_error_read': "Læsefejl fra processen.",
        'process_error_unknown': "Ukendt procesfejl",
        'process_command': "Kommando",
        'process_normal_exit': "afsluttet normalt",
        'process_crashed': "gik ned",
        'process_nonzero_exit': "{0} afsluttet med fejlkode {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Annullerer...",
        'move_cancelling': "Flytning annulleres",
        'opening_pdf': "Åbner PDF...",
        'loading_document': "Indlæser dokument...",
        'pdf_opened': "PDF åbnet",
        'pages_found_moving': "{0} sider fundet, {1} skal flyttes",
        'creating_backup': "Opretter backup...",
        'backup_description': "Sikrer original fil...",
        'backup_saved_as': "Sikret som: {0}",
        'error_format': "Fejl: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Søgning nulstillet",
        'page_header_simple': "=== Side {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Adgangskodehåndtering – Vejledning",
        'password_guide_voice': "Vejledning til adgangskodehåndtering. Læs venligst bemærkningerne.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Adgangskodehåndtering – Detaljeret vejledning</strong></p>

        <p><strong>1. Adgangskodebeskyttelse for PDF'er</strong></p>
        <ul>
        <li>Når du åbner en adgangskodebeskyttet PDF, vises en dialog, hvor du kan indtaste adgangskoden.</li>
        <li>Du kan gemme adgangskoden krypteret, så du ikke behøver at indtaste den hver gang (afkrydsningsfelt "Gem adgangskode").</li>
        <li>Med knappen "Fjern adgangskode" kan du oprette en dekrypteret kopi af PDF'en og slette adgangskoden fra databasen.</li>
        </ul>

        <p><strong>2. Master‑adgangskode</strong></p>
        <ul>
        <li>Master‑adgangskoden beskytter adgangen til alle gemte PDF‑adgangskoder.</li>
        <li><strong>Opsætning:</strong> Gå til "Indstillinger → Adgangskodehåndtering → Master‑adgangskodeindstillinger" og klik på "Opsæt master‑adgangskode". Vælg en stærk master‑adgangskode (mindst 8 tegn).</li>
        <li><strong>Ændring:</strong> Efter vellykket godkendelse kan du ændre master‑adgangskoden.</li>
        <li><strong>Fjernelse:</strong> Hvis du sletter master‑adgangskoden, slettes ALLE gemte adgangskoder uigenkaldeligt. Du kan eksportere en sikkerhedskopi først.</li>
        <li>En gang pr. session skal du godkende med master‑adgangskoden for at få adgang til beskyttede funktioner (f.eks. visning af adgangskoder).</li>
        </ul>

        <p><strong>3. Adgangskodehåndtering (liste)</strong></p>
        <ul>
        <li>Under "Indstillinger → Adgangskodehåndtering" åbner du en tabel over alle gemte PDF'er med deres krypterede adgangskoder.</li>
        <li><strong>Uden master‑adgangskode:</strong> Du kan kun slette poster – adgangskoderne forbliver skjulte.</li>
        <li><strong>Med master‑adgangskode (godkendt):</strong> Du kan se, kopiere, eksportere og slette adgangskoder.</li>
        <li><strong>Eksport:</strong> Vælg et format (JSON, CSV, TXT), og gem listen. Hvis en master‑adgangskode er angivet, kan du vælge, om adgangskoderne eksporteres i klartekst eller stadig krypteret.</li>
        <li><strong>Import:</strong> En tidligere eksporteret ZIP‑fil med alle indstillinger (inklusive adgangskoder) kan genindlæses via "Indstillinger → Eksportér/importér indstillinger". Bemærk: Eksisterende data overskrives!</li>
        </ul>

        <p><strong>4. Adgangskodegenerator</strong></p>
        <ul>
        <li>I adgangskodedialogen (f.eks. ved beskyttelse af en PDF) finder du til højre for indtastningsfeltet en terningknap 🎲.</li>
        <li>Klik på den for at åbne adgangskodegeneratoren. Du kan indstille længde, tegnsæt (store bogstaver, små bogstaver, tal, symboler) og et skilletegn for bedre læsbarhed.</li>
        <li>Den genererede adgangskode kan bruges direkte og kopieres efter behov.</li>
        </ul>

        <p><strong>5. Vigtige sikkerhedsbemærkninger</strong></p>
        <ul>
        <li>Gemte adgangskoder opbevares krypteret med AES‑256. Nøglen udledes fra din master‑adgangskode (hvis angivet) eller fra en fast værdi (uden master‑adgangskode).</li>
        <li>Uden master‑adgangskode er adgangskoderne ganske vist krypteret, men nøglen er indlejret i programmet – en angriber med adgang til dine filer kunne dekryptere dem. Derfor anbefaler vi kraftigt at bruge en master‑adgangskode.</li>
        <li>Adgangskodedatabasen ligger i mappen `Data/passwords.json`. Lav regelmæssige backups, især før du fjerner master‑adgangskoden.</li>
        <li>Hvis master‑adgangskoden mistes, er alle gemte adgangskoder uigenkaldeligt tabt.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Inverteringstilstand",
        'invert_mode_classic': "Klassisk (inverter alle farver)",
        'invert_mode_smart': "Intelligent (inverter kun lysstyrke)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Gråskala-tærskelværdi",
        'gray_threshold_10': "10% (streng)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Standard)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (blød)",
        'threshold_changed': "Tærskelværdi sat til {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Gråskala-tærskelværdi – Forklaring",
        'threshold_guide_text': "Gråskala-tærskelværdien bestemmer, hvilke pixels der i intelligent mørk tilstand betragtes som 'grå' og inverteres.\n\n"
                                "• En lav værdi (10%) inverterer kun næsten perfekte gråtoner – farvede elementer bevares fuldstændigt.\n"
                                "• En høj værdi (50%) inverterer også let farvede pixels – dette øger kontrasten, men kan forvrænge farver.\n\n"
                                "Den optimale værdi afhænger af dokumentet. For rene tekstdokumenter er 30–40% ofte ideelt, for farvet grafik snarere 10–20%.\n\n"
                                "Du kan justere værdien når som helst via menuen 'Indstillinger' – PDF'en genindlæses derefter straks.\n\n"
                                "Bemærk:\n* Fotos og billeder kan kun vises korrekt i lys tilstand!\n* Inverteringsindstillingerne vises kun, når mørk tilstand er aktiveret.",
        'threshold_guide_voice': "Gråskala-tærskelværdien bestemmer, hvor kraftigt den intelligente mørke tilstand griber ind. En lav værdi skåner farver, en høj værdi øger kontrasten.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Åbner PDF...",
        'progress_loading_document': "Indlæser dokument...",
        'progress_pdf_opened': "PDF åbnet",
        'progress_creating_backup': "Opretter backup...",
        'progress_backup_description': "Sikrer originalfil...",
        'progress_backup_created': "Backup oprettet",
        'progress_backup_saved_as': "Gemt som: {0}",
        'progress_analyzing_start': "Starter analyse...",
        'progress_searching_empty': "Søger efter tomme sider...",
        'progress_page_empty': "Side {0} er tom",
        'progress_page_keep': "Behold side {0}",
        'progress_analysis_complete': "Analyse afsluttet",
        'progress_empty_found': "Fandt {0} tomme sider",
        'progress_current_page': "Aktuel side",
        'progress_mark_delete': "Markeres til sletning",
        'progress_range_selected': "Sideområde {0}-{1}",
        'progress_deleting_pages': "Sletter {0} sider",
        'progress_creating_new_pdf': "Opretter ny PDF...",
        'progress_transferring_pages': "Overfører sider",
        'progress_keeping_page': "Side {0} beholdes ({1}/{2})",
        'progress_saving_pdf': "Gemmer PDF...",
        'progress_optimizing': "Optimerer filstørrelse...",
        'progress_finalizing': "Finaliserer...",
        'progress_new_size': "Ny størrelse: {0:.2f} MB",
        'progress_cancelling': "Annullerer...",
        'progress_cancel_message': "{0} annulleres",
        'progress_pages_found_moving': "Fandt {0} sider, {1} til flytning",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analyserer PDF...",
        'ocr_status_optimizing': "Billedoptimering kører...",
        'ocr_status_recognizing': "Tekstgenkendelse i gang...",
        'ocr_status_embedding': "Indlejrer tekst...",
        'ocr_status_finalizing': "Finaliserer PDF...",

        # PDF-Laden
        'progress_preparing': "Forbereder...",
        'progress_loading': "Indlæser PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Sletter sider...",
        'progress_moving_title': "Flytter sider...",
        'pages_found': "Sider fundet",
        'progress_creating_new_order': "Opretter ny rækkefølge...",
        'progress_sorting_pages': "Sorterer sider...",
        'progress_moving_to_begin': "Flytter {0} sider til begyndelsen",
        'progress_transferring_count': "Overfører {0} sider",
        'progress_transferring_before_target': "Overfører sider før målet",
        'progress_moving_pages': "Flytter {0} sider",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_backup_",
        'filename_protected_suffix': "_beskyttet_",
        'filename_copy_suffix': "_Kopi",
        'filename_page_single': "_Side_",
        'filename_page_range': "_Sider_",
        'filename_export_page': "_Side_{0:03}",
        'filename_export_range': "_Sider_{0}-{1}",
        'filename_export_multiple': "_Sider_{0}",
        'filename_with_text': "_med_Tekst",
        'filename_with_signature': "_med_Underskrift",
        'filename_with_image': "_med_Billede",
        'filename_with_forms': "_med_Former",
        # ---------------------------------------------------------
        # Zentrale Verwaltung des Formats der Zeitstempel
        # z.B. bei Änderung von %Y%m%d_%H%M%S auf %Y-%m-%d_%H.%M.%S
        # könnte hier vom User angepasst werden
        # ---------------------------------------------------------
        'filename_timestamp_format': "%Y%m%d_%H%M%S",
        'filename_timestamp_micro': "%Y%m%d_%H%M%S_%f",

        # ============================================
        # 56. ANSICHT – BUTTONLEISTE EIN-/AUSBLENDEN
        # ============================================
        'view_toggle_navbar': "Vis knapbjælke",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Alle sider kan ikke slettes",
		'pages_cannot_delete_last_page': 'Den sidste side kan ikke slettes!',
		'pages_cannot_delete_all_pages': 'Der skal være mindst én side tilbage i dokumentet!',
		'delete_pages_confirm': 'Er du sikker på, at du vil slette {0} sider?',
		'delete_pages_confirm_voice': 'Er du sikker på, at du vil slette {0} sider?',
		'pages_deleted': '{0} sider blev slettet.',
		'warning': 'Advarsel',
		'error': 'Fejl',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Ingen formular valgt",
        'form_customized': "Formular tilpasset",

        # ===========================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Vælg",
        'btn_use': "Brug",
        'master_password_for_spasswords': "For at gemme og bruge adgangskoder skal du først oprette en hovedadgangskode.\n\nVil du oprette hovedadgangskoden nu?",
        'open_saved_dialog_title': "Åbn gemt fil",
        'open_saved_question': "Vil du åbne den gemte fil nu?",
        'password': "Adgangskode",
        'password_manager_master_required': "Adgangskodeadministratoren er kun tilgængelig, hvis der er oprettet en hovedadgangskode.\n\nVil du oprette hovedadgangskoden nu?",
        'password_master_required_for_select': "For at kunne vise og vælge gemte adgangskoder skal du først godkende med din hovedadgangskode.\n\nVil du godkende nu?",
        'password_not_available': "Den valgte adgangskode er ikke tilgængelig eller kunne ikke dekrypteres.",
        'password_options_title': "Adgangskodeindstillinger",
        'password_save_choice_change': "Opret ny adgangskode",
        'password_save_choice_keep': "Brug eksisterende adgangskode",
        'password_save_choice_none': "Gem ukrypteret",
        'password_save_hint': "Opret først en hovedadgangskode for at gemme adgangskoder sikkert.",
        'password_save_master_required': "Gem adgangskode (kun muligt med hovedadgangskode)",
        'password_save_question': "Den aktuelle PDF er adgangskodebeskyttet. Vil du bruge den eksisterende adgangskode, oprette en ny eller gemme ukrypteret?",
        'password_select': "Vælg adgangskode",
        'password_select_none': "Ingen adgangskode valgt.\n\nVælg venligst en adgangskode fra listen.",
        'password_select_one': "Vælg venligst præcis én adgangskode.\n\nDu har markeret flere adgangskoder.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_backup",
        'filename_insert_suffix': "_med_indsættelse",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_sider_slettet",
        'filename_pages_moved': "_sider_flyttet",
        'filename_rotated_all_suffix': "_alle_sider_drejet",
        'filename_rotated_suffix': "_side_drejet",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfiguration af filnavne ved ændringer af PDF",
        'filename_keep_suffixes': "Behold tidligere udvidelser (f.eks. _med_tekst)",
        'filename_keep_suffixes_false': "Erstat",
        'filename_keep_suffixes_true': "Behold",
        'filename_preview_label': "Forhåndsvisning af filnavn:",
        'filename_preview_overwrite_hint': "Forhåndsvisning ikke tilgængelig – originalen overskrives.",
        'filename_separator': "Adskillelsestegn mellem ord",
        'filename_separator_none': "Intet adskillelsestegn",
        'filename_separator_space': "Mellemrum ( )",
        'filename_separator_underscore': "Understregning (_)",
        'filename_settings_saved': "Filnavneindstillinger gemt",
        'filename_settings_title': "Filnavneformatering og backup",
        'filename_timestamp_position': "Placering af tidsstempel",
        'filename_timestamp_position_after': "Efter grundnavnet",
        'filename_timestamp_position_before': "Helt forrest",
        'filename_timestamp_position_end': "Til sidst",
        'filename_use_timestamp': "Brug tidsstempel",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Adfærd ved ændringer:</b><ul><li>Sletning og indsættelse af sider</li><li>Indsættelse af tekst, signatur, billede og former</li><li>OCR</li></ul></html>",
        'backup_section': "Backup for sideoperationer (Sletning, Flytning)",
        'behavior_info': "Bemærk: Ved 'Overskriv original' ignoreres tidsstempler og suffikser – filen bevarer sit navn.",
        'behavior_new_file': "Opret altid ny fil (med tidsstempel og suffiks)",
        'behavior_overwrite': "Overskriv original (ingen ny fil)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Alle sider blev drejet.\n\nOriginalen forblev uændret.\nNy fil: {0}",
        'all_pages_rotated_voice': "Alle sider drejet, ny fil oprettet.",
        'empty_pages_deleted_new_file': "{0} tomme sider blev slettet.\n\nOriginalen forblev uændret.\nNy fil: {1}",
        'empty_pages_deleted_voice': "{0} tomme sider slettet, ny fil oprettet.",
        'ocr_keep_original': "Behold original (åbn manuelt senere)",
        'ocr_new_file_question': "Den nye søgbare PDF blev gemt som:\n{0}\n\nVil du åbne den nu?",
        'ocr_open_new': "Åbn ny OCR-fil",
        'ocr_original_kept': "Den originale fil forbliver åben. OCR-filen er gemt.",
        'page_deleted_new_file': "Side {0} blev slettet.\n\nOriginalen forblev uændret.\nNy fil: {1}",
        'page_deleted_voice': "Side {0} slettet, ny fil oprettet.",
        'page_rotated_new_file': "Side {0} blev drejet.\n\nOriginalen forblev uændret.\nNy fil: {1}",
        'page_rotated_voice': "Side {0} drejet, ny fil oprettet.",
        'pages_deleted_new_file': "Der blev slettet {0} sider.\n\nDen originale fil forblev uændret.\nNy fil: {1}",
        'pages_deleted_new_file_voice': "{0} sider slettet, ny fil oprettet.",
        'pages_inserted_new_file': "Der blev indsat {0} sider.\n\nDen originale fil forblev uændret.\nNy fil: {1}",
        'pages_inserted_new_file_ask': "Der blev indsat {0} sider.\n\nOriginalen forblev uændret.\nNy fil: {1}\n\nVil du åbne den nu?",
        'pages_inserted_voice_new': "{0} sider indsat, ny fil oprettet.",
        'pages_moved_new_file': "Der blev flyttet {0} sider.\n\nDen originale fil forblev uændret.\nNy fil: {1}",
        'pages_moved_new_file_voice': "{0} sider flyttet, ny fil oprettet.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Vis ikke igen",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Backup-indstilling</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Backup TIL</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Ved alle ændringer, der overskriver originalen</strong> (tekst, signatur, billede, form, OCR, drejning, indsættelse, slet/flyt sider) oprettes <strong>automatisk en backup med tidsstempel</strong>, før ændringen anvendes.</p>
                <p style="margin: 5px 0 5px 20px;">• Backuppen ligger ved siden af den originale fil (f.eks. <code>Dokument_backup_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Hvis du desuden har aktiveret indstillingen <strong>„Overskriv original“</strong>, oprettes der også en backup.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Backup FRA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Der oprettes ingen backup</strong> – hverken ved overskrivning eller ved sideoperationer.</p>
                <p style="margin: 5px 0 5px 20px;">• Den originale fil kan gå uigenkaldeligt tabt ved overskrivning.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Anbefales kun til erfarne brugere!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> Backup-indstillingen er uafhængig af indstillingen „Overskriv original“. Du kan kombinere begge.<br>
                Du kan skjule denne meddelelse permanent.
            </div>
        </div>
        """,
        'backup_info_title': "Backup-adfærd",
        'backup_info_voice': "Meddelelse om backup-adfærd ved sideoperationer. Backup til overskriver original, backup fra opretter ny fil.",
        'show_backup_info': "Info om backup-indstilling",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Vis ikke igen",
        'overwrite_enable_backup': "Aktivér backup (anbefales)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Overskriv original</p>
            <p>Hvis du aktiverer denne indstilling, gemmes ændringer (tekst, signatur, billede, form, OCR, drejning, indsættelse) <strong>direkte i originalen</strong> – <strong>der oprettes ingen ny fil</strong>.</p>
            <p>• Filnavnet forbliver uændret.<br>
            • Tidsstempler og suffikser ignoreres.<br>
            • <strong>Uden backup kan originalen gå uigenkaldeligt tabt.</strong></p>
            <p style="color: #FFD700;">Anbefaling: Aktivér desuden backup-indstillingen for at få automatiske sikkerhedskopier.</p>
        </div>
        """,
        'overwrite_info_title': "Overskriv original",
        'overwrite_info_voice': "Advarsel: Overskriv original – ingen ny fil. Backup anbefales.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Der blev indsat {0} sider.\n\nDen originale fil blev overskrevet.\nDer blev oprettet en backup.",
        'pages_inserted_overwrite_no_backup': "Der blev indsat {0} sider.\n\nDen originale fil blev overskrevet.\nDer blev IKKE oprettet en backup.",
        'texts_saved_overwrite_with_backup': "Ændringerne blev gemt i originalen.\n\nDer blev oprettet en backup.",
        'texts_saved_overwrite_no_backup': "Ændringerne blev gemt i originalen.\n\nDer blev IKKE oprettet en backup.",
        'texts_crosses_saved_new_file': "{0} {1} og {2} {3} blev indsat.\n\nDen originale fil forblev uændret.\nDer blev oprettet en ny fil.\n\nDen nye PDF indlæses...",
        'texts_saved_new_file': "{0} {1} blev indsat.\n\nDen originale fil forblev uændret.\nDer blev oprettet en ny fil.\n\nDen nye PDF indlæses...",
        'crosses_saved_new_file': "{0} {1} blev indsat.\n\nDen originale fil forblev uændret.\nDer blev oprettet en ny fil.\n\nDen nye PDF indlæses...",
        'elements_saved_new_file': "{0} elementer blev indsat.\n\nDen originale fil forblev uændret.\nDer blev oprettet en ny fil.\n\nDen nye PDF indlæses...",
        'signatures_saved_overwrite_with_backup': "Signatur(erne) blev gemt i originalen.\n\nDer blev oprettet en backup.",
        'signatures_saved_overwrite_no_backup': "Signatur(erne) blev gemt i originalen.\n\nDer blev IKKE oprettet en backup.",
        'images_saved_overwrite_with_backup': "Billedet(erne) blev gemt i originalen.\n\nDer blev oprettet en backup.",
        'images_saved_overwrite_no_backup': "Billedet(erne) blev gemt i originalen.\n\nDer blev IKKE oprettet en backup.",
        'forms_saved_overwrite_with_backup': "Formen(erne) blev gemt i originalen.\n\nDer blev oprettet en backup.",
        'forms_saved_overwrite_no_backup': "Formen(erne) blev gemt i originalen.\n\nDer blev IKKE oprettet en backup.",
        'signatures_saved_new_file': "{0} signaturer blev indsat.\n\nDen originale fil forblev uændret.\nDer blev oprettet en ny fil.\n\nDen nye PDF indlæses...",
        'images_saved_new_file': "{0} billeder blev indsat.\n\nDen originale fil forblev uændret.\nDer blev oprettet en ny fil.\n\nDen nye PDF indlæses...",
        'forms_saved_new_file': "{0} former blev indsat.\n\nDen originale fil forblev uændret.\nDer blev oprettet en ny fil.\n\nDen nye PDF indlæses...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Advarsel: Denne PDF indeholder drejede sider. Placeringen kan afvige.",
        'page_rotated_warning_title': "Drejet side registreret",
        'page_rotated_warning_message': "Den aktuelle side {0} er drejet {1}°.\n\nIndsættelse af elementer på drejede sider understøttes ikke.\n\nVil du dreje siden til oprejst position nu?",
        'page_rotated_warning_voice': "Advarsel: Siden er drejet. Drej den venligst først.",
        'paste_on_rotated_page_simple_warning': "Indsættelse på side {0} ikke mulig!\n\nDenne side er drejet {1}°.\n\nDrej venligst først siden til 0° (Menu: Rediger → Ret side op).\n\nAdvarsel:\nDet tidligere kopierede element går tabt, hvis du ikke gemmer før drejning af siden.",
        'paste_on_rotated_page_voice': "Indsættelse afbrudt. Siden er drejet. Ret venligst siden op først.",
        'page_rotated_cancel': "Annuller",
        'page_rotated_rotate_until_upright': "Drej siden gentagne gange (indtil oprejst)",
        'page_rotated_now_upright': "Siden er nu oprejst. Du kan nu indsætte.",
        'page_rotated_still_not_upright': "Siden kunne ikke drejes til oprejst position. Ret venligst manuelt.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Hjælp: Ret drejede sider",
        'help_rotated_pages_voice': "Hjælp til korrigering af drejede sider åbnes.",
        'btn_help': "Hjælp",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problem: Drejet side – Indsættelse fungerer ikke korrekt</p>

            <p>Hvis indsættelse af tekster, signaturer eller former på en drejet side ikke fungerer korrekt, kan du rette siden med en ekstern PDF-editor.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Løsning med eksternt værktøj (f.eks. macOS Forhåndsvisning)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Eksporter side</strong><br>
                &nbsp;&nbsp;Klik i menuen på <strong>Fil → Eksporter som sider</strong> eller brug en anden metode til at gemme den ønskede side som en enkelt PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Åbn siden i eksternt program</strong><br>
                &nbsp;&nbsp;Åbn den eksporterede PDF i en PDF-editor (f.eks. <strong>macOS Forhåndsvisning</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Drej siden</strong><br>
                &nbsp;&nbsp;Drej siden, så den står oprejst (i Forhåndsvisning: <strong>Værktøjer → Drej</strong> eller <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Gem</strong><br>
                &nbsp;&nbsp;Gem den korrigerede side (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Indsæt siden igen i det originale dokument</strong><br>
                &nbsp;&nbsp;Gå tilbage til PDFDarkView og indsæt den korrigerede side på den ønskede position:<br>
                &nbsp;&nbsp;<strong>Rediger → Indsæt sider</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativ: Drej siden i originalen</p>
                <p style="margin: 5px 0 5px 20px;">• Brug den indbyggede drejefunktion (<strong>Rediger → Drej side</strong>) til trinvist at korrigere siden.<br>
                • Efter hver drejning kan du kontrollere, om indsættelse nu fungerer.<br>
                • Dette er ofte den hurtigere løsning – prøv det først!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> Hvis du ofte støder på drejede sider, kan du permanent skjule advarslen i indsættelsesdialogen.<br>
                Placeringen kan da afvige – brug kun denne indstilling, hvis du kender konsekvenserne.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Ret sider op",
        'menu_rotate_normalize_tooltip': "Drej side eller nulstil til 0°",
        'normalize_current_page': "Bring aktuel side i oprejst position (sæt til 0°)",
        'normalize_all_pages': "Bring alle sider i oprejst position (sæt til 0°)",
        'page_normalized': "Side {0} blev bragt i oprejst position.",
        'all_pages_normalized': "Alle sider blev bragt i oprejst position.",
        'page_already_upright': "Side {0} er allerede oprejst.",
        'all_pages_already_upright': "Alle sider er allerede oprejste.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF'en indeholder ingen søgbar tekst.</p><p>Vil du udføre OCR for at eksportere til {0}?</p>",
        'export_ocr_voice': "PDF'en indeholder ingen tekst. OCR er påkrævet for eksport til {0}.",
        'export_no_ocr_possible': "Eksport uden OCR ikke mulig. Udfør venligst OCR via menuen.",
        'ocr_failed_export_not_possible': "OCR mislykkedes. Eksport kan ikke udføres.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF åbnes i Forhåndsvisning. Start venligst udskrivningsprocessen der.",
        'print_preview_manual': "PDF blev åbnet. Udfør venligst udskrivningskommandoen manuelt (f.eks. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Sammenflet PDF'er",
        'merge_pdfs': "Sammenflet PDF'er",
        'merge_progress_title': "Sammenfletter PDF'er...",
        'merge_pdfs_list': "PDF'er i rækkefølge (Træk og slip for at sortere)",
        'merge_add_pdf': "Tilføj PDF",
        'merge_remove': "Fjern",
        'merge_move_up': "Op",
        'merge_move_down': "Ned",
        'merge_pdfs_info': "💡 Tip: Du kan ændre rækkefølgen ved at trække og slippe",
        'merge_no_pdfs': "Ingen PDF'er valgt. Klik på 'Tilføj PDF'.",
        'merge_info': "{0} PDF'er valgt (ca. {1} sider)",
        'merge_open_file': "Åbn fil",
        'merge_merge': "Sammenflet",
        'merge_error': "Fejl ved sammenfletning",
        'merge_min_two_pdfs_error': "Vælg venligst mindst to PDF-filer til sammenfletning.",
        'merge_select_pdfs': "Vælg PDF'er til sammenfletning",
        'merge_error_file': "Fejl ved behandling",
        'merge_cancelled': "Sammenfletning blev annulleret",
        'merge_preparing': "Forbereder...",
        'merge_processing': "Behandler PDF {0} af {1}",
        'merge_saving': "Gemmer sammenflettet PDF...",
        'merge_complete': "Færdig!",
        'merge_success_title': "Sammenfletning lykkedes",
        'merge_success_voice': "{0} PDF'er blev succesfuldt sammenflettet.",
        'merge_success_message': "{0} PDF'er blev succesfuldt sammenflettet.\n\nDet nye dokument har nu {1} sider.\n\nNy fil:\n{2}\n\nGemmeplacering:\n{3}\n{2}\n\nVil du åbne denne PDF?",
        'replace_file_title': "Erstat fil?",
        'replace_file_message': "Der er allerede åbnet en PDF. Vil du erstatte den med den nye fil?",
        'btn_yes': "Ja",
        'btn_no': "Nej",
        'filename_merge_suffix': "sammenflettet",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Åbner {0}...",
        'progress_merge_reading': "Læser {0}...",
        'progress_merge_adding': "Tilføjer {0} sider...",
        'progress_merge_optimizing': "Optimerer PDF...",
        'progress_merge_writing': "Skriver PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "lukning af PDF",
        'action_close_window': "lukning af vinduet",
        'action_open_new_pdf': "åbning af en ny PDF",
        'action_quit_app': "afslutning af programmet",
        'changes_saved': "Ændringerne blev gemt.",
        'file_close_title': "Luk PDF-fil",
        'save_before_action': "Skal ændringerne gemmes før {0}? Ja eller Nej?",
        'save_before_action_voice': "Skal ændringerne gemmes før {0}? Ja eller Nej?",
        'save_before_close_question': "Skal ændringerne gemmes før lukning? Ja eller Nej?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Søgbar PDF oprettet:\n\n{0}\n\n<b>prøv igen om nødvendigt",
        "ocr_rotate_title": "Juster sider før OCR",
        "ocr_rotate_question": "PDF'en indeholder roterede sider.\nVil du justere alle sider til 0° før OCR?\nDette forbedrer tekstgenkendelsen betydeligt.",
        "ocr_rotate_yes": "Ja, juster",
        "ocr_rotate_no": "Nej, start OCR direkte",
        "ocr_rotate_voice": "PDF'en indeholder roterede sider. Skal alle sider justeres før OCR?",
        "ocr_not_performed_message": "Ingen tekst til stede. Udfør venligst OCR (menu \"Rediger\" → \"Udfør OCR\" eller tast Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR-indstillinger",
        "ocr_language_btn": "Vælg OCR-sprog",
        "ocr_language": "OCR-sprog",
        "ocr_language_current": "Aktuelt sprog:",
        "ocr_param_info": "Information om parameter",

        "ocr_force_ocr_label": "Tving OCR",
        "ocr_deskew_label": "Korriger skævhed",
        "ocr_clean_label": "Rens billede",
        "ocr_oversample_label": "Opløsning (DPI)",
        "ocr_pagesegmode_label": "Sideopdeling",
        "ocr_oem_label": "OCR-motor tilstand",
        "ocr_optimize_label": "PDF-komprimering",
        "ocr_jobs_label": "Parallelle processer",
        "ocr_verbose_label": "Log detaljegrad",

        "ocr_force_ocr_tooltip": "Tving OCR på hver side, selvom der allerede er tekst",
        "ocr_deskew_tooltip": "Automatisk juster skæve scanninger",
        "ocr_clean_tooltip": "Fjern støj og artefakter fra billedet",
        "ocr_oversample_tooltip": "Opret skalering af billede før OCR til denne DPI",
        "ocr_pagesegmode_tooltip": "Bestemmer, hvordan siden opdeles i tekstområder",
        "ocr_oem_tooltip": "Vælger Tesseracts OCR-motor",
        "ocr_optimize_tooltip": "Komprimeringsniveau for output PDF",
        "ocr_jobs_tooltip": "Antal parallelle OCR-processer",
        "ocr_verbose_tooltip": "Detaljegrad for log-output",
        "ocr_settings_explain_btn": "Forklaring",

        "ocr_force_ocr_explain": "Tvinger tekstgenkendelse på <b>hver</b> side, selvom den allerede indeholder tekst.\n\nAnbefaling: <b>Til</b> for scannede PDF'er, <b>Fra</b> for native PDF'er med allerede eksisterende tekst.",

        "ocr_deskew_explain": "Korrigerer let skæve scanninger (op til ca. 5°).\n\nAnbefaling: <b>Til</b> for scannede dokumenter, <b>Fra</b> hvis siderne allerede er perfekt lige.",

        "ocr_clean_explain": "Fjerner støj, prikker og små artefakter fra billedet.\n<b>VIGTIGT:</b> For arabiske, thailandske eller vietnamesiske tekster med diakritiske tegn (prikker over/under bogstaver) bør denne indstilling <b>deaktiveres</b>, ellers kan vigtige tegn gå tabt.",

        "ocr_oversample_explain": "Skalerer billedet <b>før</b> tekstgenkendelse til den angivne DPI.<br><br>• <b>72-150 DPI:</b> Meget hurtigt, men lav genkendelsesrate<br>• <b>200-300 DPI:</b> Optimalt område (Standard: 300)<br>• <b>400+ DPI:</b> Næsten ingen bedre genkendelse, men væsentligt større filer<br><br>Anbefaling: 300 DPI til komplekse skrifter (arabisk, kinesisk, japansk), 200 DPI til vestlige sprog.",

        "ocr_pagesegmode_explain": "Bestemmer, hvordan Tesseract opdeler siden i tekstområder.\n\n• <b>3 - Automatisk (Standard):</b> Godt til blandede layouts\n• <b>4 - Enkelt kolonne:</b> Til tekster med én kolonne\n• <b>5 - Lodret blok:</b> Til lodrette skrifter (japansk, kinesisk)\n• <b>6 - Ensartet tekstblok:</b> Optimalt til flydende tekst uden kolonner\n• <b>11 - Råt billede:</b> Til dårlige scanninger / håndskrift\n\nAnbefaling: <b>6</b> til enkle tekstdokumenter, <b>3</b> til komplekse layouts.",

        "ocr_oem_explain": "Vælger Tesseracts OCR-motor.\n\n• <b>0 - Legacy:</b> Gammel motor (hurtig, men mindre præcis)\n• <b>1 - LSTM:</b> Neural motor (langsommere, men mere præcis)\n• <b>2 - Legacy + LSTM:</b> Kombinerer begge resultater\n• <b>3 - Standard (LSTM foretrækkes):</b> Bedste valg til de fleste tilfælde\n\nAnbefaling: <b>3</b> til maksimal genkendelsespræcision.",

        "ocr_optimize_explain": "Komprimerer output PDF.\n\n• <b>0:</b> Ingen optimering (hurtigste behandling)\n• <b>1:</b> Let optimering (godt kompromis)\n• <b>2:</b> Moderat optimering\n• <b>3:</b> Kraftig optimering (mindste fil, men langsommere)\n\nAnbefaling: <b>1</b> til daglig brug.",

        "ocr_jobs_explain": "Antal parallelle processer til OCR.\n\n• <b>1:</b> Langsomt, men laveste hukommelsesforbrug\n• <b>4-8:</b> Optimalt til moderne flerkerneprocessorer\n• <b>12+:</b> Næsten ingen hurtigere behandling ved højt hukommelsesforbrug\n\nAnbefaling: Antal CPU-kerner (f.eks. <b>4</b> på 4-kerne systemer).",

        "ocr_verbose_explain": "Detaljegrad for log-output i konsollen.\n\n• <b>0:</b> Ingen output\n• <b>1:</b> Fremskridt og statusmeddelelser\n• <b>2:</b> Detaljeret output\n• <b>3:</b> Fuld debug-output (meget omfattende)\n\nAnbefaling: <b>1</b> til normal drift.",

        "ocr_reset_title": "Indstillinger nulstillet",
        "ocr_reset_message": "Alle OCR-indstillinger er blevet nulstillet til standardværdierne.",
        "info_tooltip": "Mere information om denne parameter",
        "ocr_reset_defaults": "Nulstil til standard",

        "ocr_psm_0": "Automatisk (Legacy-motor)",
        "ocr_psm_1": "Automatisk kolonnedetektion",
        "ocr_psm_3": "Automatisk (Standard)",
        "ocr_psm_4": "Enkelt kolonne",
        "ocr_psm_5": "Lodret blok",
        "ocr_psm_6": "Ensartet tekstblok",
        "ocr_psm_7": "Enkelt tekstlinje",
        "ocr_psm_8": "Enkelt ord",
        "ocr_psm_11": "Råt billede (ingen layoutanalyse)",

        "ocr_oem_0": "Legacy-motor (hurtig)",
        "ocr_oem_1": "LSTM-motor (neural, præcis)",
        "ocr_oem_2": "Legacy + LSTM kombineret",
        "ocr_oem_3": "Standard (LSTM foretrækkes)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR-sprog...",
        "ocr_language_title": "Vælg OCR-sprog",
        "ocr_language_instruction": "Vælg sprog til tekstgenkendelse (OCR).\nBemærk: Flere sprog går ud over ydeevne og nøjagtighed!\nDu opnår de bedste resultater, hvis du kun vælger ét sprog.",
        "ocr_language_predefined": "Foruddefinerede kombinationer",
        "ocr_language_custom": "Brugerdefineret...",
        "ocr_language_selected": "Valgte OCR-sprog",
        "ocr_language_changed": "OCR-sprog ændret til {0}",
        "ocr_language_auto_detect": "Tilgængelige sprog detekteres automatisk.",
        "ocr_language_none_found": "Ingen Tesseract-sprogdata fundet! Installer venligst sprogpakker (f.eks. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Brugerdefineret sprogvalg",
        "ocr_language_available": "Tilgængelige sprog (installeret):",
        "ocr_language_select_hint": "Vælg et eller flere sprog:",
        "ocr_language_confirm": "Anvend",
        "ocr_language_reset": "Nulstil til standard (deu+eng+vie)",
        "ocr_language_priorities": "Anbefalede sprog (forudinstalleret):",

        "select_all_languages": "Vælg alle",
        "clear_all_languages": "Ryd valg",
        "install_language_packs": "Installer manglende sprogpakker...",
        "install_hint": "💡 Tip: Ikke alle sprog er installeret på dit system. Via denne knap får du hjælp til installation.",
        "ocr_language_install_title": "Installation af Tesseract-sprogpakker",

        "ocr_missing_languages": "Manglende OCR-sprogpakker",
        "ocr_missing_languages_message": "Følgende valgte sprog er ikke installeret på dit system:\n\n{0}\n\nInstaller venligst de manglende sprogpakker (se hjælp under 'Installationshjælp').\n\nVil du åbne installationshjælpen nu?",
        "ocr_missing_languages_voice": "Manglende sprogpakker. Installer venligst de manglende sprog.",
        "ocr_install_help_now": "Åbn hjælp",
        "ocr_continue_anyway": "Forsøg alligevel",
        "ocr_language_error_title": "OCR-sprog fejl",
        "ocr_language_error_message": "Fejl ved tekstgenkendelse: {0}\n\nKontroller dine OCR-sprogindstillinger (Indstillinger → OCR-sprog).",
        "ocr_install_help_button": "Installationshjælp",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Installer Tesseract-sprogpakker</p>

        <p>For at OCR kan fungere på et bestemt sprog, skal de tilsvarende sprogdata være installeret på dit system. Følg vejledningen til dit operativsystem:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Åbn <strong>Terminal</strong> (Finder → Programmer → Værktøjer → Terminal).</li>
        <li>Installer alle tilgængelige sprog med:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
>(Dette kan tage et par minutter.)</li>
        <li>Eller kun enkelte sprog (f.eks. vietnamesisk):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
Ved nuværende Homebrew-versioner skal <code>*.traineddata</code> muligvis downloades manuelt (se nedenfor).</li>
        <li>Efter installation: Luk denne dialog og åbn OCR-sprogvalget igen – de nye sprog vises automatisk.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Åbn en terminal (Ctrl+Alt+T).</li>
        <li>Installer det ønskede sprog, f.eks. til vietnamesisk:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
Vigtige sprogkoder: <code>deu</code> (tysk), <code>eng</code> (engelsk), <code>vie</code> (vietnamesisk), <code>spa</code> (spansk), <code>fra</code> (fransk), <code>ita</code> (italiensk), <code>nld</code> (hollandsk), <code>fin</code> (finsk), <code>swe</code> (svensk), <code>nor</code> (norsk).</li>
        <li>Vis alle tilgængelige pakker:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manuel)</p>
        <ol>
        <li>Download de ønskede <code>*.traineddata</code>-filer fra:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
(f.eks. <code>vie.traineddata</code> til vietnamesisk).</li>
        <li>Kopier filerne til Tesseracts sprogmappe, normalt:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
(Tilpas ved individuel installation.)</li>
        <li>Genstart applikationen (eller åbn OCR-sprogvalget igen).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativ til alle systemer</p>
        <ul>
        <li>Installer <strong>OCRmyPDF</strong> og <strong>Tesseract</strong> med en pakkeadministrator efter eget valg. De fleste installationer indeholder allerede nogle standardsprog (engelsk, tysk, fransk).</li>
        <li>Manglende sprog kan installeres når som helst – OCR-sprogvalget viser kun de faktisk eksisterende sprog.</li>
        </ul>

        <hr>
        <p><b>✅ Efter installation:</b> Ingen genstart af applikationen nødvendig – de nytilføjede sprog vises straks på listen.</p>
        <p><b>📖 Hjælp til sprogkoder:</b> En komplet liste findes i <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract-dokumentationen</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans-skrifttyper",
        "info_noto_font_voice": "Installeringsvejledning til Noto Sans-skrifttyper",
        "btn_info_noto_font_install": "Skrifttypeinfo",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Sådan installeres de gratis Noto-skrifttyper fra Google</h2>

        <p><strong>Noto-skrifttyperne</strong> er en open-source skrifttypefamilie fra Google. Deres mål er at <em>"ikke se tofu"</em> (dvs. ingen tomme bokse □) og korrekt vise hvert tegn fra Unicode-standarden. De er det ideelle supplement til applikationer, der skal vise tekster på mange forskellige sprog.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Installation på macOS</h3>

        <p><strong>Metode 1: Med Homebrew (for avancerede)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metode 2: Via "Font Book" (Anbefalet)</strong></p>

        <ol>
        <li>Download den officielle skrifttypepakke:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Udpak ZIP-filen</li>
        <li>Kopier filerne til <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Installation på Windows (10 & 11)</h3>

        <p><strong>Metode 1: Microsoft Store (Anbefalet)</strong><br>
        Søg efter "Google Noto Fonts" eller "Noto Sans" og klik på <strong>Installer</strong>.</p>

        <p><strong>Metode 2: Manuel installation</strong></p>

        <ol>
        <li>Download:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Udpak ZIP</li>
        <li>Vælg .ttf / .otf filer</li>
        <li>Højreklik → <strong>Installer</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        eller<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Navn\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Installation på Linux</h3>

        <ul style='list-style: none; padding-left: 0;'>

        <li><strong>Ubuntu / Debian:</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo apt update && sudo apt install fonts-noto-core fonts-noto-cjk fonts-noto-extra</pre>
        </li>

        <li><strong>Fedora:</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo dnf install google-noto-sans-cjk-ttc</pre>
        </li>

        <li><strong>Arch:</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo pacman -S noto-fonts noto-fonts-cjk</pre>
        </li>

        <li><strong>openSUSE:</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo zypper install google-noto-fonts</pre>
        </li>

        </ul>

        <p>Verifikation:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Administrer bogmærker",
        "bookmark_add": "Tilføj bogmærke",
        "bookmark_add_tooltip": "Gem nuværende side som bogmærke",
        "bookmark_remove": "Fjern bogmærke",
        "bookmark_remove_tooltip": "Slet det markerede bogmærke",
        "bookmark_remove_all": "Fjern alle",
        "bookmark_remove_all_tooltip": "Slet alle bogmærker i denne PDF",
        "bookmark_jump": "Gå til bogmærke",
        "bookmark_jump_tooltip": "Gå til den valgte side",
        "bookmark_name": "Navn",
        "bookmark_page": "Side",
        "bookmark_no_bookmarks": "Ingen bogmærker til stede.\nKlik på 'Tilføj' for at gemme den aktuelle side som bogmærke.",
        "bookmark_added": "Bogmærke for side {0} tilføjet: {1}",
        "bookmark_removed": "Bogmærke fjernet: {0}",
        "bookmark_all_removed": "Alle bogmærker er fjernet.",
        "bookmark_name_default": "Side {0}",
        "bookmark_name_prompt": "Navn til bogmærket:\n(lang tekst forkortes til 50 tegn)",
        "bookmark_name_prompt_title": "Bogmærkenavn",
        "bookmark_confirm_remove_all": "Er du sikker på, at du vil fjerne alle {0} bogmærker?",
        "menu_bookmarks": "Bogmærker",
        "bookmark_manage": "Administrer bogmærker",
        "bookmark_next": "Næste bogmærke",
        "bookmark_prev": "Forrige bogmærke",
        "bookmark_page_display": "Side {0}",
        "bookmark_exists": "Der findes allerede et bogmærke for denne side med dette navn.",
        "bookmark_select_first": "Vælg først et bogmærke.",
        "bookmark_confirm_remove": "Er du sikker på, at du vil fjerne bogmærket 'Side {0}: {1}'?",
        "bookmark_jumped_to": "Gået til bogmærke '{0}' på side {1}.",
        "bookmark_jumped_to_voice": "Bogmærke {0}, side {1}",
        "btn_close": "Luk",

        "bookmark_list": "Dine bogmærker",
        "bookmark_rename": "Omdøb bogmærke",
        "bookmark_rename_tooltip": "Skift navnet på det valgte bogmærke",
        "bookmark_rename_title": "Omdøb bogmærke",
        "bookmark_rename_prompt": "Nyt navn til bogmærke på side {0}:\n(maks. 50 tegn)",
        "bookmark_renamed": "Bogmærke '{0}' er omdøbt til '{1}'.",
        "bookmark_item_tooltip": "Side {0}: {1}\nDobbeltklik for at gå",
        "bookmark_name_exists_question": "Der findes allerede et bogmærke med navnet '{0}' på denne side.\nOmdøb alligevel?",

        "context_bookmarks": "Bogmærker",
        "context_bookmark_add_here": "Tilføj bogmærke for denne side",
        "context_bookmarks_existing": "Eksisterende bogmærker:",
        "context_bookmarks_jump": "Gå til bogmærke:",
        "context_bookmarks_none": "Ingen bogmærker til stede",
        "context_bookmarks_clear_all": "Fjern alle {0} bogmærker",

        "bookmark_search_placeholder": "Søg i bogmærker... (navn eller side)",
        "bookmark_search_results": "%d bogmærker fundet for \"%s\"",
        "bookmark_no_search_results": "Ingen bogmærker fundet for \"%s\"",
        "bookmark_no_search_results_label": "Ingen resultater for \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Rediger PDF-metadata",
        "metadata_title": "Titel",
        "metadata_title_placeholder": "Dokumenttitel",
        "metadata_title_tooltip": "Dokumentets titel (vises i titellinjen)",
        "metadata_author": "Forfatter",
        "metadata_author_placeholder": "Forfatterens navn",
        "metadata_author_tooltip": "Dokumentets skaber",
        "metadata_subject": "Emne",
        "metadata_subject_placeholder": "Dokumentets emne",
        "metadata_subject_tooltip": "En kort beskrivelse af indholdet",
        "metadata_keywords": "Nøgleord",
        "metadata_keywords_placeholder": "Nøgleord adskilt af kommaer",
        "metadata_keywords_tooltip": "Nøgleord til kategorisering af dokumentet",
        "metadata_creator": "Skaber",
        "metadata_creator_placeholder": "Applikation, der har oprettet PDF'en",
        "metadata_creator_tooltip": "Softwaren, som dokumentet er oprettet med",
        "metadata_producer": "Producent",
        "metadata_producer_placeholder": "Applikation, der har konverteret PDF'en",
        "metadata_producer_tooltip": "Softwaren, der konverterede PDF'en",
        "metadata_creation_date": "Oprettelsesdato",
        "metadata_creation_date_tooltip": "Datoen for dokumentoprettelse",
        "metadata_mod_date": "Ændringsdato",
        "metadata_mod_date_tooltip": "Datoen for sidste ændring",
        "metadata_pdf_info": "📄 PDF-information",
        "metadata_pages": "Antal sider",
        "metadata_file_size": "Filstørrelse",
        "metadata_pdf_version": "PDF-version",
        "metadata_encrypted": "Krypteret",
        "metadata_encrypted_yes": "Ja (adgangskodebeskyttet)",
        "metadata_encrypted_no": "Nej",
        "metadata_reload": "📂 Genindlæs fra PDF",
        "metadata_reset": "Forkast ændringer",
        "metadata_reloaded": "Metadata er genindlæst fra PDF'en.",
        "metadata_reset_done": "Alle metadatafelter er blevet nulstillet.",
        "metadata_no_file": "Ingen PDF-fil indlæst.",
        "metadata_save_error": "Fejl ved lagring af metadata",
        "metadata_saved": "Metadata er blevet gemt succesfuldt.",
        "metadata_pdf_version_unknown": "PDF (ukendt)",
        "metadata_saved_message": "Metadata er blevet gemt succesfuldt.",
        "metadata_saved_voice": "Metadata gemt.",

        "metadata_custom": "🔧 Brugerdefineret metadata",
        "metadata_custom_placeholder": "{\n  \"mit_felt\": \"min værdi\",\n  \"andet_felt\": 123\n}",
        "metadata_custom_tooltip": "JSON-format til brugerdefineret metadata (valgfrit)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Skabelon \"{0}\" valgt - Dobbeltklik for at indsætte",
        "text_use_template": "Brug tekstblok",
        "text_type": "Type",
        "text_search_templates": "Søg i tekstblokke...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Eksport / Import information",
        "qsettings_export_import_info_html": """<!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <style>
        body {
            margin: 0;
            padding: 16px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #2d2d2d;
            color: #f0f0f0;
            line-height: 1.5;
        }
        h3 {
            color: #FFD700;
            font-size: 20px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 15px;
            border-bottom: 2px solid #FFD700;
            padding-bottom: 8px;
        }
        h4 {
            color: #87CEEB;
            font-size: 18px;
            font-weight: bold;
            margin-top: 25px;
            margin-bottom: 10px;
        }
        ul {
            margin-top: 5px;
            margin-bottom: 15px;
            list-style-type: none;
            padding-left: 5px;
        }
        li {
            margin-bottom: 8px;
            font-size: 15px;
            line-height: 1.6;
        }
        .category {
            color: #98FB98;
            font-weight: bold;
            font-size: 16px;
            margin-right: 15px;
        }
        .detail {
            color: #FFFFFF;
            margin-left: 30px;
        }
        .checkmark {
            color: #4CAF50;
            font-weight: bold;
            margin-right: 8px;
        }
        .warning {
            color: #FF6B6B;
            font-weight: bold;
        }
        .box {
            background-color: #3a3a3a;
            border-left: 4px solid #FFD700;
            padding: 12px 16px;
            margin: 15px 0;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        }
        .box strong {
            display: block;
            margin-bottom: 8px;
        }
        .box ul {
            margin: 5px 0 0 0;
            padding-left: 20px;
        }
        .box li {
            margin-bottom: 4px;
        }
        code {
            background-color: #444;
            padding: 4px 8px;
            border-radius: 5px;
            font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
            font-size: 13px;
            display: inline-block;
            margin-top: 6px;
        }
        hr {
            border: none;
            border-top: 1px solid #555;
            margin: 20px 0;
        }
        </style>
        </head>
        <body>

        <h3>📦 Hvad eksporteres? (Oversigt)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Generelle applikationsindstillinger</span></li>
            <li class="detail">• Mørk/Lys tilstand</li>
            <li class="detail">• Mørk tilstand invertering for billeder</li>
            <li class="detail">• Grå tærskelværdi</li>
            <li class="detail">• Sprog</li>
            <li class="detail">• Vinduesgeometri</li>
            <li class="detail">• Zoom-tilstand</li>
            <li class="detail">• Navigation (Navigationslinje synlig)</li>
            <li class="detail">• Taleoutput (til/fra)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Backup-indstillinger</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Filnavngivning (Tidsstempel, Separator, Suffikser)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Indstillinger for indsættelse af</span></li>
            <li class="detail">• Signaturer</li>
            <li class="detail">• Tekst &amp; tekstblokke</li>
            <li class="detail">• Krydser, billeder og former</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR-indstillinger</span></li>
            <li class="detail">• Sprog</li>
            <li class="detail">• Tving OCR · Sidetilstand</li>
            <li class="detail">• Billedforbehandling: Ret skævhed, Rens, Oversampling</li>
            <li class="detail">• Antal parallelle job</li>
            <li class="detail">• Inverteringstilstand</li>
            <li class="detail">• Grå tærskelværdi</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Bogmærker</span></li>
            <li class="detail">• Alle bogmærker pr. PDF-fil (Side, Navn, Oprettelsestid)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Adgangskodedatabase</span></li>
            <li class="detail">• Gemte PDF-adgangskoder (valgfrit krypteret eller almindelig tekst)</li>
            <li class="detail">• Master-adgangskode hash (hvis angivet)</li>
            <li class="detail">• Verifikationsdata</li>
        </ul>

        <h4>⚠️ Vigtige bemærkninger</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Ved import:</strong>
            <ul>
                <li><span class="warning">➜ ALLE nuværende indstillinger vil blive fuldstændigt overskrevet</span></li>
                <li>• Genstart af applikationen er obligatorisk</li>
                <li>• Eksisterende signaturer, tekstblokke og bogmærker vil blive erstattet</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Master-adgangskode og eksporttilstand:</strong>
            <ul>
                <li>• Når master-adgangskoden er aktiv, kan du vælge:</li>
                <li>  - <span style="color: #98FB98;"><strong>Dekrypteret</strong></span> (adgangskoder er i almindelig tekst i ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Krypteret</strong></span> (kan kun læses med master-adgangskode på målsystemet)</li>
                <li>• Master-adgangskodehashen gemmes <strong>altid</strong> krypteret</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Sikkerhedsadvarsel:</strong>
            <ul>
                <li>• Den eksporterede ZIP-fil indeholder følsomme data (<strong>adgangskoder, bogmærker, signaturer</strong>)</li>
                <li>• Opbevar den sikkert (f.eks. krypteret USB-stick, adgangskodeadministrator)</li>
                <li>• Hvis filen går tabt, er gemte PDF-adgangskoder uigenkaldeligt tabt</li>
            </ul>
        </div>

        <h4>📁 Eksportformat</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Indstillingerne gemmes i en enkelt ZIP-fil:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Denne ZIP indeholder den fulde <code>settings.json</code> (fra din konfiguration) samt eventuelt indlejrede signaturbilledfiler og krypterede adgangskoder.
        </p>

        </body>
        </html>""",

        # ============================================
        # 84. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programmet afsluttes",

    }
