import marshal

print('====================================================')
print('           Welcome to AK Code Protection Tool       ')
print('           Telegram : https://t.me/AKHacking1       ')
print('           Github : https://github.com/ak404z       ')
print('====================================================')

file = input("Enter Python file name: ").strip()  # إزالة أي مسافات زائدة

try:
    # فتح وقراءة محتوى الملف
    with open(file, 'r', encoding='utf-8') as f:
        open_file = f.read()

    # تحويل الكود إلى Bytecode باستخدام Marshal
    com = compile(open_file, file, 'exec')
    coding = marshal.dumps(com)

    # إنشاء ملف الإخراج
    output_file = "cod_" + file

    with open(output_file, 'w', encoding='utf-8') as cod:
        cod.write('import marshal\n')
        cod.write("exec(marshal.loads(" + repr(coding) + "))")

    # طباعة تأكيد نجاح التشفير
    print(f'File encrypted successfully : {output_file}')

except FileNotFoundError:
    print("Error: File not found. Please check the file name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# إضافة input() لمنع الخروج الفوري
input("\nPress Enter to exit...")
