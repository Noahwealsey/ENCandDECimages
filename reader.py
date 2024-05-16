import time
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

import numpy as np

import AES as aes
import DES as des
import RSA as rsa
import tripleDES as des3

import cv2 as cv

img = cv.imread('target.jpg')
cv.imshow('gae', img)
b, g, r = cv.split(img)

r_text = '\n'.join([' '.join(map(str, row)) for row in r])
g_text = '\n'.join([' '.join(map(str, row)) for row in g])
b_text = '\n'.join([' '.join(map(str, row)) for row in b])


with open('red_data.txt', 'w') as file:
    file.write(r_text)

with open('green_data.txt', 'w') as file:
    file.write(g_text)

with open('blue_data.txt', 'w') as file:
    file.write(b_text)


def Write(data, fpath):
    with open(fpath, "wb") as file:
        file.write(data)

    with open(fpath, "wb") as file:
        file.write(data)

    with open(fpath, "wb") as file:
        file.write(data)




def AES(r_data, g_data, b_data, aes_key):

    aes_r_encrypted = aes.encrypt(r_data, aes_key)
    aes_g_encrypted = aes.encrypt(g_data, aes_key)
    aes_b_encrypted = aes.encrypt(b_data, aes_key)

    with open("Secrets/AES/aes_r_encrypted.enc", "wb") as file:
        file.write(aes_r_encrypted)

    with open("Secrets/AES/aes_g_encrypted.enc", "wb") as file:
        file.write(aes_g_encrypted)

    with open("Secrets/AES/aes_b_encrypted.enc", "wb") as file:
        file.write(aes_b_encrypted)


def DES(r_data, g_data, b_data, des_key):
    des_r_encrypted = des.encrypt(r_data, des_key)
    des_g_encrypted = des.encrypt(g_data, des_key)
    des_b_encrypted = des.encrypt(b_data, des_key)

    with open("Secrets/DES/des_r_encrypted.enc", "wb") as file:
        file.write(des_r_encrypted)

    with open("Secrets/DES/des_g_encrypted.enc", "wb") as file:
        file.write(des_g_encrypted)

    with open("Secrets/DES/des_b_encrypted.enc", "wb") as file:
        file.write(des_b_encrypted)

def RSA(r_data, g_data, b_data, rsa_key):
    rsa_r_encrypted = rsa.encrypt(r_data, rsa_key)
    rsa_g_encrypted = rsa.encrypt(g_data, rsa_key)
    rsa_b_encrypted = rsa.encrypt(b_data, rsa_key)

    with open("Secrets/RSA/rsa_r_encrypted.enc", "wb") as file:
        file.write(rsa_r_encrypted)

    with open("Secrets/RSA/rsa_g_encrypted.enc", "wb") as file:
        file.write(rsa_g_encrypted)

    with open("Secrets/RSA/rsa_b_encrypted.enc", "wb") as file:
        file.write(rsa_b_encrypted)


def DES3(r_data, g_data, b_data, des3_key):
    tripleDES_r_encrypted = des3.encrypt(r_data, des3_key)
    tripleDES_g_encrypted = des3.encrypt(g_data, des3_key)
    tripleDES_b_encrypted = des3.encrypt(b_data, des3_key)

    with open("Secrets/3DES/tripleDES_r_encrypted.enc", "wb") as file:
        file.write(tripleDES_r_encrypted)

    with open("Secrets/3DES/tripleDES_g_encrypted.enc", "wb") as file:
        file.write(tripleDES_g_encrypted)

    with open("Secrets/3DES/tripleDES_b_encrypted.enc", "wb") as file:
        file.write(tripleDES_b_encrypted)

def generate_pdf_with_table(encryption_times):
    df = pd.DataFrame.from_dict(encryption_times, orient='index', columns=['Encryption Time (s)'])

  
    df['Algorithm'] = df.index
    df = df[['Algorithm', 'Encryption Time (s)']]
    table_data = [df.columns.to_list()] + df.values.tolist()

  
    plt.figure(figsize=(8, 4))
    plt.bar(df['Algorithm'], df['Encryption Time (s)'], color='skyblue')
    plt.xlabel('Algorithm')
    plt.ylabel('Encryption Time (s)')
    plt.title('Encryption Time for Each Algorithm')
    plt.xticks(rotation=45)
    plt.tight_layout()

  
    plt.savefig('encryption_times.png')


    pdf_filename = 'encryption_times.pdf'
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    table = Table(table_data)


    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table.setStyle(style)

    
    doc.build([table])

    print(f"PDF generated successfully: {pdf_filename}")


def main():
    
    with open('red_data.txt', 'r') as file:
        r_data = file.read()

    with open('green_data.txt', 'r') as file:
        g_data = file.read()

    with open('blue_data.txt', 'r') as file:
        b_data = file.read()

    r_data = r_data.encode()
    g_data = g_data.encode()
    b_data = b_data.encode()
    
    # Measure encryption time for DES
    s_aes = time.time()
    aes_key_size = 256
    aes_key = aes.generate_aes_key(aes_key_size)
    AES(r_data, g_data, b_data, aes_key)
    e_aes = time.time()
    time_aes = e_aes - s_aes

    # Measure encryption time for DES
    s_des = time.time()
    des_key = des.generate_des_key()
    DES(r_data, g_data, b_data, des_key)
    e_des = time.time()
    time_des = e_des - s_des

    # Measure encryption time for Triple DES
    s_des3 = time.time()
    des3_key = des3.generate_triple_des_key()
    DES3(r_data, g_data, b_data, des3_key)
    e_des3 = time.time()
    time_des3 = e_des3 - s_des3
    
    
    rsa_key_size = 1024
    rsa_key = rsa.generate_rsa_keypair(rsa_key_size)
    print(rsa_key)
    # RSA(r_data, g_data, b_data, rsa_key)
    #  the subject is too big for RSA. even
    #  after adjusting the chunk size the entire code crashes.
    #  enable at your own risk 
    print("Encryption times for each algorithm:")
    print(f"AES: {time_aes} seconds")
    print(f"DES: {time_des} seconds")
    print(f"Triple DES: {time_des3} seconds")

    generate_pdf_with_table({'AES': time_aes, 'DES': time_des, 'Triple DES': time_des3})

    with open("Secrets/AES/aes_r_encrypted.enc", "rb") as file:
        aes_r_encrypted = file.read()

    with open("Secrets/AES/aes_g_encrypted.enc", "rb") as file:
        aes_g_encrypted = file.read()

    with open("Secrets/AES/aes_b_encrypted.enc", "rb") as file:
        aes_b_encrypted = file.read()

    aes_r_decrypted = aes.decrypt(aes_r_encrypted, aes_key)
    aes_g_decrypted = aes.decrypt(aes_g_encrypted, aes_key)
    aes_b_decrypted = aes.decrypt(aes_b_encrypted, aes_key)


if __name__ == "__main__":
   main()
