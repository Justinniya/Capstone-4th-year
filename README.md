# Phinma 4th Year Student Monitoring System

## Pagtugyan
Ini nga proyekto isa ka web-based monitoring system nga nagabulig sa pag-manage sang impormasyon sang mga 4th-year nga estudyante sa Phinma UI. Gamit ang Flask para sa backend kag MySQL bilang database, ini nga sistema nagapadali sang pag-track sang status sang estudyante.

## Mga Kinahanglanon
Antes magsugod, siguruhon nga may ara ka sang masunod nga software kag dependencies:
- **Python 3**
- **Flask**
- **Flask-MySQLdb**
- **MySQL Database (XAMPP o WAMP)**
- **Bootstrap 5**

## Paano I-setup
1. **I-install ang mga kinahanglanon**
   ```sh
   pip install -r requirements.txt
   ```
2. **I-configure ang database**
   - Himoa ang database nga `monitoring_database`
   - I-import ang `database.sql` nga file para makuha ang table structure
3. **I-run ang application**
   ```sh
   python app.py
   ```
   Bisitaha ang `http://127.0.0.1:5000/` para makita ang application.

## Mga Features
- **Landing Page** - Login page para sa mga authorized users.
- **Dashboard** - Main interface nga nagapakita sang tanan nga estudyante.
- **Pagdugang sang Estudyante** - Form para makadugang sang bagong estudyante sa database.
- **Graduating List** - Listahan sang mga estudyante nga naga-graduate.
- **Pag-update sang Data** - Edit kag update sang impormasyon sang estudyante.
- **Session Management** - Authentication system para sa seguridad sang users.

## Paano Gamiton
- **Pag-login**: Gumamit sang admin credentials (`admin/admin`).
- **Pagdugang sang estudyante**: I-kompleto ang form kag i-submit.
- **Pag-update sang estudyante**: I-click ang "Update" button sa dashboard.
- **Pag-confirm sang graduation**: I-click ang "Confirm" kung ang estudyante qualified na mag-graduate.

Pag-explain sang Code

app.py

Flask Initialization: Ang Flask amo ang nagapatakod sang web application.

Database Configuration: Ang app.config nagaset sang MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, kag MYSQL_DB para maka-connect sa MySQL database.

Session Management: Ginagamit ang session para sa authentication kag security.

Routes:

/ - Landing page nga nagapakita sang login form.

/login - Nagacheck sang credentials kag nagapadulong sa dashboard kung sakto.

/dashboard - Nagapakita sang tanan nga estudyante kag ilang impormasyon.

/add_students - Form para makadugang sang bagong estudyante sa database.

/update/<id> - Ginapa-edit ang impormasyon sang estudyante.

/graduating_list - Listahan sang mga estudyante nga naga-graduate.

/confirm/<id> - Ginatransfer ang estudyante sa graduation list.

landing.html

Nagapakita sang login form.

May Bootstrap design para sa responsiveness.

May flash messages para magpakita sang success o error messages.

dashboard.html

Nagapakita sang listahan sang mga estudyante.

May buttons para sa pag-edit kag pag-confirm sang graduation status.

add_students.html

Form nga naga-require sang UI ID, Name, Age, Year, Section, Major, Units, kag Status.

May validation gamit ang JavaScript para malikawan ang empty fields.

graduating_list.html

Nagapakita sang listahan sang mga nag-graduate nga estudyante.

update.html

Nagahatag sang form para ma-update ang impormasyon sang isa ka estudyante.

Ginagamit ang value="{{ result[x] }}" para ma-populate ang existing data.


## File Structure
```
monitoring-system/
│── static/
│   ├── css/
│   │   ├── dashboard.css
│   │   ├── add_students.css
│   │   ├── graduating_list.css
│   ├── img/
│── templates/
│   ├── landing.html
│   ├── dashboard.html
│   ├── add_students.html
│   ├── graduating_list.html
│   ├── update.html
│── app.py
│── requirements.txt
│── database.sql
```

## Developer Notes
- Siguruhon nga nagdagan ang MySQL database antes i-run ang Flask app.
- Ang session-based authentication nagaseguro nga ang user lang nga authorized ang makasulod.
- Kung may problema sa database, siguruhon nga naka-configure sang husto ang `app.config` sa `app.py`.
