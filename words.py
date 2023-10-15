bingo_title = "BINGO"
spanish_foods = ['Gratis','La comida', 'La fresa', 'El limón', 'La manzana', 'La uva',
 'El brócoli','La cebolla', 'El maíz', 'El queso', 'Las papas', 'La hamburguesa',
 'El arroz', 'El pan', 'El helado', 'La carne', 'El bistec', 'El pollo', 'El tocino',
 'El pescado', 'El agua', 'El hielo', 'El café', 'El jugo', 'La Leche']
english_foods = ['Free', 'Food', 'Strawberry', 'Lemon', 'Apple', 'Grape',
 'Broccoli', 'Onion', 'Corn', 'Cheese', 'Potatoes', 'Hamburger', 'Rice', 
 'Bread', 'Ice Cream', 'Meat', 'Steak', 'Chicken', 'Bacon', 'Fish', 'Water',
  'Ice', 'Coffee', 'Juice', 'Milk']

english_body = ['Free','Body','Hand','Finger','Foot','Toes','Leg','Arm','Head','Hair','Face','Eye','Nose','Boogers','Ear','Mouth','Teeth','Tongue','Blood','Knee','Shoulder','Stomach','Heart','Elbow','Brain',]
spanish_body = ['Gratis','El Cuerpo','La Mano','El Dedo','El Pie','Los Dedos De Pie','La Pierna','El Brazo','La Cabeza','El Pelo','La Cara','El Ojo','La Nariz','Los Mocos','La Oreja','La Boca','Los Dientes','La Lengua','La Sangre','La Rodilla','El Hombro','El Estómago','El Corazón','El Codo','El Cerebro',]

words = [spanish_foods, english_foods, spanish_body, english_body]

MAX_LEN = max(len(spanish_foods),len(english_foods))
