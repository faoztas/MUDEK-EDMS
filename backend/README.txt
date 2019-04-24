Web Projesinin Çalıştırılma ve kullanım aşamaları:

- Proje Repository
    git clone git@github.com:zyavuz610/accreditation_for_MUDEK.git

- Virtualenv kurulumu
    pip install virtualenv

- env kurulumu
    python3 -m venv tenv

- env actif edilmesi
    source tenv/bin/activate

- Proje için gerekli paketlerin kurulması 
    pip install -r requirements.txt

- Tabloların oluşturulması
    ./manage.py makemigrations

- Tabloların Uygulanması
    ./manage.py migrate

- User oluşturulması (Süperuser)
    ./manage createsuperuser

- Projenin çalıştırılması
    ./manage runserver

- Web browserda açma
    http://127.0.0.1:8000/edms/login/

- Kullanıcı adı ve şifresi ile giriş yaptıktan sonra /admin paneline giderek Ders Sorumlusu oluşturarak oluşturulan ders sorumlusuna ders ataması yapılır

- Oluşturulan ders sorumlusu ile giriş yapılarak lessons sayfasıyla bu ders sorumlusuna ait derler görüntülenir ve içeriği düzenlenir.

- Reset-password ekranında mail adresi girilerek parola link ile yenilenir 

- change password ile ekranda parola değişikliği yapılabilir.


Android Projesinin Çalıştırılma aşamaları

- Proje Repository
    git clone git@github.com:zyavuz610/accreditation_for_MUDEK.git

- Proje çalıştırılması
    Android Studio ile çalıştırılabilir.
