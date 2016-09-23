rmdir /s /q "release"
pyinstaller.exe --distpath "release" --workpath "tmp" --specpath "tmp" --clean -F -y -n Tera -i "icon.ico" -c --uac-admin main.py
rmdir /s /q "tmp"
xcopy "data" "release\data" /i /q /e /y