#Zadatak 6

filename = "SMSSpamCollection.txt"

ham_word_counts = []
spam_word_counts = []
spam_exclamation_count = 0

with open(filename, "r", encoding="utf-8") as file:
    for line in file:

        parts = line.strip().split("\t", 1)
        if len(parts) < 2:
            continue
        
        label, message = parts[0], parts[1]
        
        word_count = len(message.split())
        
        if label == "ham":
            ham_word_counts.append(word_count)
        elif label == "spam":
            spam_word_counts.append(word_count)
            
            if message.strip().endswith("!"):
                spam_exclamation_count += 1


avg_ham = sum(ham_word_counts) / len(ham_word_counts) if ham_word_counts else 0
avg_spam = sum(spam_word_counts) / len(spam_word_counts) if spam_word_counts else 0

print(f"Prosječan broj riječi (ham): {avg_ham:.2f}")
print(f"Prosječan broj riječi (spam): {avg_spam:.2f}")
print(f"Broj spam poruka koje završavaju uskličnikom: {spam_exclamation_count}")