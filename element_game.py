import random

# Define 100 elements with their strengths and weaknesses
elements = {
    'fire': ['water', 'earth', 'ice', 'wind', 'lightning'],
    'water': ['earth', 'fire', 'air', 'rock', 'sand'],
    'earth': ['air', 'water', 'lightning', 'metal', 'wind'],
    'air': ['earth', 'fire', 'lightning', 'rock', 'ice'],
    'lightning': ['earth', 'water', 'air', 'metal', 'sand'],
    'ice': ['fire', 'lightning', 'air', 'rock', 'sand'],
    'metal': ['fire', 'lightning', 'earth', 'water', 'air'],
    'wind': ['earth', 'metal', 'rock', 'ice', 'water'],
    'rock': ['metal', 'lightning', 'ice', 'air', 'water'],
    'sand': ['water', 'ice', 'rock', 'metal', 'air'],
    # Adding more elements to reach 100
    'poison': ['fire', 'ice', 'lightning', 'air', 'earth'],
    'shadow': ['lightning', 'fire', 'holy', 'metal', 'ice'],
    'holy': ['shadow', 'poison', 'dark', 'fire', 'lightning'],
    'dark': ['holy', 'light', 'shadow', 'fire', 'ice'],
    'light': ['dark', 'shadow', 'poison', 'earth', 'water'],
    'nature': ['fire', 'ice', 'poison', 'metal', 'lightning'],
    'thunder': ['earth', 'water', 'metal', 'rock', 'ice'],
    'magma': ['water', 'ice', 'air', 'sand', 'wind'],
    'crystal': ['metal', 'lightning', 'rock', 'fire', 'earth'],
    'void': ['light', 'holy', 'dark', 'shadow', 'poison'],
    'cosmic': ['void', 'dark', 'shadow', 'poison', 'metal'],
    'plasma': ['water', 'ice', 'earth', 'metal', 'crystal'],
    'sound': ['crystal', 'metal', 'ice', 'rock', 'air'],
    'time': ['space', 'void', 'cosmic', 'light', 'dark'],
    'space': ['time', 'void', 'cosmic', 'gravity', 'light'],
    'gravity': ['space', 'air', 'wind', 'rock', 'metal'],
    'quantum': ['time', 'space', 'void', 'cosmic', 'lightning'],
    'nuclear': ['metal', 'crystal', 'rock', 'fire', 'plasma'],
    'radiation': ['nature', 'poison', 'life', 'metal', 'crystal'],
    'life': ['death', 'poison', 'dark', 'shadow', 'void'],
    'death': ['life', 'holy', 'light', 'nature', 'poison'],
    'dream': ['reality', 'void', 'shadow', 'cosmic', 'time'],
    'reality': ['dream', 'void', 'quantum', 'space', 'time'],
    'chaos': ['order', 'reality', 'dream', 'void', 'cosmic'],
    'order': ['chaos', 'void', 'shadow', 'dark', 'cosmic'],
    'void': ['reality', 'order', 'chaos', 'light', 'holy'],
    'aether': ['void', 'cosmic', 'quantum', 'space', 'time'],
    'spirit': ['void', 'shadow', 'dark', 'death', 'poison'],
    'mind': ['dream', 'void', 'shadow', 'spirit', 'reality'],
    'soul': ['mind', 'spirit', 'dream', 'void', 'light'],
    'blood': ['water', 'life', 'fire', 'metal', 'ice'],
    'bone': ['rock', 'metal', 'earth', 'ice', 'fire'],
    'flesh': ['nature', 'life', 'blood', 'fire', 'ice'],
    'steel': ['fire', 'metal', 'lightning', 'rock', 'earth'],
    'glass': ['rock', 'crystal', 'sound', 'metal', 'lightning'],
    'paper': ['rock', 'steel', 'metal', 'crystal', 'ice'],
    'scissors': ['paper', 'glass', 'flesh', 'nature', 'wood'],
    'rock_old': ['scissors', 'glass', 'crystal', 'ice', 'metal'],
    'lava': ['water', 'ice', 'rock', 'metal', 'earth'],
    'mud': ['fire', 'ice', 'air', 'rock', 'metal'],
    'dust': ['water', 'ice', 'air', 'wind', 'earth'],
    'ash': ['water', 'ice', 'air', 'wind', 'nature'],
    'smoke': ['wind', 'air', 'water', 'ice', 'lightning'],
    'mist': ['fire', 'wind', 'air', 'lightning', 'earth'],
    'cloud': ['lightning', 'fire', 'wind', 'air', 'ice'],
    'storm': ['earth', 'water', 'rock', 'metal', 'ice'],
    'hurricane': ['earth', 'rock', 'metal', 'crystal', 'ice'],
    'tornado': ['earth', 'rock', 'metal', 'crystal', 'sand'],
    'earthquake': ['air', 'wind', 'water', 'ice', 'lightning'],
    'tsunami': ['fire', 'earth', 'rock', 'metal', 'sand'],
    'volcano': ['water', 'ice', 'air', 'wind', 'nature'],
    'meteor': ['earth', 'water', 'ice', 'nature', 'life'],
    'comet': ['fire', 'ice', 'water', 'earth', 'metal'],
    'star': ['void', 'dark', 'shadow', 'cosmic', 'space'],
    'moon': ['star', 'sun', 'cosmic', 'space', 'light'],
    'sun': ['moon', 'star', 'void', 'shadow', 'dark'],
    'planet': ['comet', 'meteor', 'star', 'cosmic', 'space'],
    'galaxy': ['planet', 'star', 'void', 'cosmic', 'space'],
    'nebula': ['galaxy', 'star', 'void', 'cosmic', 'space'],
    'blackhole': ['light', 'star', 'galaxy', 'cosmic', 'space'],
    'wormhole': ['time', 'space', 'void', 'cosmic', 'quantum'],
    'dimension': ['reality', 'time', 'space', 'void', 'cosmic'],
    'multiverse': ['dimension', 'reality', 'void', 'cosmic', 'time'],
    'infinity': ['multiverse', 'void', 'cosmic', 'quantum', 'time'],
    'eternity': ['time', 'infinity', 'multiverse', 'void', 'cosmic'],
    'genesis': ['void', 'chaos', 'order', 'cosmic', 'quantum'],
    'apocalypse': ['life', 'nature', 'order', 'cosmic', 'reality'],
    'creation': ['void', 'chaos', 'genesis', 'cosmic', 'quantum'],
    'destruction': ['creation', 'life', 'nature', 'order', 'reality'],
    'balance': ['chaos', 'order', 'creation', 'destruction', 'void'],
    'harmony': ['chaos', 'order', 'balance', 'creation', 'destruction'],
    'discord': ['harmony', 'balance', 'order', 'creation', 'reality'],
    'fusion': ['fission', 'nuclear', 'quantum', 'plasma', 'fire'],
    'fission': ['fusion', 'nuclear', 'quantum', 'plasma', 'energy'],
    'energy': ['matter', 'void', 'quantum', 'plasma', 'lightning'],
    'matter': ['energy', 'void', 'quantum', 'gravity', 'space'],
    'antimatter': ['matter', 'energy', 'void', 'quantum', 'reality'],
    'darkmatter': ['light', 'matter', 'energy', 'void', 'gravity'],
    'darkenergy': ['matter', 'energy', 'void', 'quantum', 'gravity'],
    'singularity': ['blackhole', 'void', 'quantum', 'time', 'space'],
    'consciousness': ['mind', 'soul', 'dream', 'reality', 'void'],
    'existence': ['void', 'reality', 'consciousness', 'dream', 'time'],
    'nonexistence': ['existence', 'reality', 'void', 'dream', 'consciousness']
}

# Get all element names
all_elements = list(elements.keys())

# Ensure we have at least 100 elements
if len(all_elements) < 100:
    print(
        f"Warning: Only {len(all_elements)} elements available. Adding more...")
    # Fill to 100 with numbered generic elements
    for i in range(1, 101 - len(all_elements) + 1):
        generic_element = f"element_{i}"
        elements[generic_element] = random.sample(
            all_elements, min(5, len(all_elements)))
        all_elements.append(generic_element)

print(f"🎮 WELCOME TO THE 100-ELEMENT BATTLE GAME! 🎮")
print(f"Total elements available: {len(all_elements)}")
print("\n" + "="*50)

# Get user input
users_input = input("Please enter an element: ").lower().strip()

# Validate if element exists
if users_input not in elements:
    print(f"❌ '{users_input}' is not a valid element!")
    print(
        f"Available elements: {', '.join(all_elements[:20])}... (and {len(all_elements)-20} more)")
else:
    computer_choice = random.choice(all_elements)

    print("\n" + "="*50)
    print(f"💻 Computer chose: {computer_choice}")
    print(f"👤 You chose: {users_input}")
    print("="*50 + "\n")

    # Determine winner
    if computer_choice == users_input:
        print("🤝 TIE! 🤝")
        print("Both elements are equal in power!")

    elif computer_choice in elements[users_input]:
        print("🎉🎉🎉 YOU WON! 🎉🎉🎉")
        print(f"✨ {users_input} defeats {computer_choice}! ✨")

    elif users_input in elements[computer_choice]:
        print("💀💀💀 YOU LOST! 💀💀💀")
        print(f"⚔️ {computer_choice} defeats {users_input}! ⚔️")

    else:
        print("⚠️ INVALID MATCHUP! ⚠️")
        print("These elements don't have a clear advantage over each other!")
        print("Try a different element next time!")

print("\n" + "="*50)
print("Thanks for playing the 100-Element Game! 🎮")
