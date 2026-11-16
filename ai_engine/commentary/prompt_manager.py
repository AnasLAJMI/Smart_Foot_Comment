
def build_commentary_prompt(event, language="ar"):

    if language == "ar":
        prompt = f"""
أنت معلق كرة قدم محترف في بث تلفزيوني مباشر.

علّق على الحدث التالي بأسلوب عربي طبيعي وحماسي:

نوع الحدث: {event['event_type']}
الدقيقة: {event['minute']}
الوصف: {event['description']}

قواعد مهمة:
- إذا كان الحدث Goal، يجب أن تصف هدفاً تم تسجيله بالفعل.
- لا تصف الهدف على أنه مجرد تسديدة أو محاولة.
- استخدم أسماء اللاعبين كما وردت في الوصف، ولا تغيّرها.
- لا تخترع أسماء أو تفاصيل غير موجودة.
- تجنب تكرار الكلمات والجمل.
- استخدم لغة عربية سليمة وأسلوب المعلقين الرياضيين.
- اكتب جملة أو جملتين قصيرتين ومتكاملتين.
- يجب أن ينتهي التعليق بعلامة ترقيم.
- أخرج التعليق فقط دون مقدمات أو شرح.
"""

    elif language == "fr":
        prompt = f"""
Tu es un commentateur de football professionnel.

Commente l'événement suivant avec un style naturel et dynamique :

Type : {event['event_type']}
Minute : {event['minute']}
Description : {event['description']}

Règles :
- Si l'événement est un Goal, décris un but déjà marqué.
- Ne transforme pas un but en simple tir ou tentative.
- N'invente aucun nom ni détail.
- Évite les répétitions.
- Utilise un style naturel de commentaire sportif télévisé.
- Écris une ou deux phrases courtes et complètes.
- Termine par une ponctuation.
- Donne uniquement le commentaire.
"""

    else:
        raise ValueError("Unsupported language")

    return prompt
