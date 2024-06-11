import hashlib

bUsername_trial = b"FRASER"

# From the keygenme-trial.py file
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"

sequence = [4, 5, 3, 6, 2, 7, 1, 8]

generated_hash = hashlib.sha256(bUsername_trial).hexdigest()

for i in sequence:
    key_part_dynamic1_trial += generated_hash[i]

key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

print(key_full_template_trial)