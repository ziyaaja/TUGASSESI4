def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "Draw"
    elif (player1_choice == "batu" and player2_choice == "gunting") or \
         (player1_choice == "gunting" and player2_choice == "kertas") or \
         (player1_choice == "kertas" and player2_choice == "batu"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def main():
    print("Permainan Batu-Gunting-Kertas")
    print("Pilihan: batu, gunting, kertas")
    
    player1_choice = input("Player 1, masukkan pilihan Anda: ").lower()
    player2_choice = input("Player 2, masukkan pilihan Anda: ").lower()
    
    if player1_choice not in ["batu", "gunting", "kertas"] or player2_choice not in ["batu", "gunting", "kertas"]:
        print("Pilihan tidak valid. Silakan masukkan kembali.")
        return
    
    winner = determine_winner(player1_choice, player2_choice)
    print(winner)

if __name__ == "__main__":
    main()
