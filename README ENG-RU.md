USE RELEASED VERSION IF YOU DON'T KNOW WHAT YOU ARE DOING / ПОЛЬЗУЙТЕСЬ ВЕРСИЕЙ ИЗ РЕЛИЗОВ ЕСЛИ НЕ ЗНАЕТЕ ЧТО ДЕЛАЕТЕ

>What is this software?
>
  This is an opencv2 script I created for my bachelor's thesis while studying at North Kazakhstan University named after M. Kozybaev.
  It is created to calculate surface area of polar mesospheric clouds in 30-degree longtitudal sectors on CIPS images
  This means, that if you combine surface area of all 12 sectors you can get overall surface for selected image.
  Script is operating with whole folders of images rather than singular images and very simple to use as is.
>How do I use it?
  1. Go to https://lasp.colorado.edu/aim/download/pmc/l3a/ and download data of interest.
  2. You will get a zip folder which will contain another folder with images (level_3) -- i recommend renaming it to reflect corresponding year and hemisphere, but first you should unzip it somewhere else.
  3. Check if the path to the folder you used to unzip your data is fully in Latin, since the script will crash if the path at any point is not in Latin.
  4. This means if your path looks loke that "C:\Users\Иван\Documents\Img\North\2022" -- script will complain about path uninterity (with a flashing messages in cmd) and terminate itself, so use instead something like "C:\Users\Vetrtillit\Documents\Img\North\2022"
  5. If you path is correct, launch the Calculate executive you downloaded from GitHub, you will be asked to choose a folder -- shoose the folder you just unzipped (clearing it up is not necessary, script will sort files by itself).
  6. Then you will be asked which background image script should use -- click "Север" if your images are for nothern hemisphere and "Юг" is, respectively, for southern. WARNING: incorrect background image will create massive deviation in calculated data.
  7. If all was done correctly, in a few seconds script will terminate itself after successful execution and "surface_area.xlsx" file should be created in your selected folder. That's it, how you will use this book is now up to you.

Thank you for using my script! I will appreciate if you let me know what discoveries you have made with it, will be sincerely grateful for mentioning in your scienfic works (my full name is Roman Alexandrovich Kleksin or Kleksin R.A.) 
and will gladly answer your question and accept any feedback. 
You can contact me, aside conventional means, through Telegram: @Vetrtillit or email: fjolkunnigr@yandex.kz
The software is distributed under Creative Commons license, which means you can use it as you wish and modify in any ways because I despise the concept of intellectual property, it's free to use. 

> Для чего эта программа?
> 
  Это скрипт opencv2, который я написал для своего диплома, пока учился в Северо-Казахстанском Университете им. М. Козыбаева.
  Создан он был, чтобы расчитывать площадь серебристых облаков в 30-градусных долготных секторах на изображениях CIPS.
  Если вам нужна общая площадь для каждого изображения -- вы сможете сложить результаты для секторов чтобы получить общую площадь.
  Скрипт работает сразу с папками, вместо отдельных изображений, и в целом весьма прост к использованию.
> Как мне его использовать?
  1. Скачайте нужные вам данные с https://lasp.colorado.edu/aim/download/pmc/l3a/
  2. Вы получите zip-папку, в которой будет через несколько других вложена папка с изображениями (level_3) -- рекомендую её переименовать, чтобы название отражало год и полушарие на изображениях, однако для начала папку нужно распаковать.
  3. Обратите внимание, чтобы папка, в которую вы распаковываете папку с изображениями, содержала в своем пути только латиницу, так как скрипт будет завершаться с ошибкой если хоть один символ в пути не латинский.
  4. Иначе говоря, если ваш путь выглядит вот так: "C:\Users\Иван\Documents\Img\North\2022" -- скрипт пожалуется на нарушение целостности пути (ошибку вы даже не успеете прочесть в командной строке) и закроется.
  5. Поэтому лучше иметь путь такого рода: "C:\Users\Vetrtillit\Documents\Img\North\2022"
  6. Если путь допустимый, запустите исполнительный файл Calculcate, который вы скачали с GitHub, в возникшем окне выберите распакованную вами ранее папку с изображениями (её необязательно чистить от архивов .gz/.nz, скрипт сам все отфильтрует).
  7. Всплывет еще одно окно, которое спросит вас, какое фоновое изображение использовать -- выбирайте в соответствие с полушарием, для которого получали данные. ВАЖНО: неправильно выбранный фон может создать сильное отклонение в вычислениях, будьте внимательны
  8. Через несколько секунд скрипт завершится после успешного исполнения и файл "surface_area.xlsx" должен быть создан в выбранной вами папке с изображениями. Вот и все, что вы дальше делаете с этими данными -- ваше дело.

Спасибо за использование моего скрипта! Буду признателен, если дадите знать об открытиях, что были совершены с его помощью, и искренне благодарен за упоминание в ваших работах (мое полное имя -- Клексин Роман Александрович или Клексин Р.А.),
также с радостью отвечу на ваши вопросы и приму любые отзывы.
Со мной можно связаться, помимо очевидных методов, с помощью Телеграма: @Vetrtillit или email: fjolkunnigr@yandex.kz
Программа распространяется под лицензией Creative Commons, что означает, что использовать и модифицировать её можно как угодно -- мне неприятна сама коцнепция интеллектуальной собственности, пользуйтесь свободно.
