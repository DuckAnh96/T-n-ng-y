from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
inventory = {}

@app.route('/')
def display_inventory():
    message = request.args.get('message', '')
    return render_template('inventory.html', inventory=inventory, message=message)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    if name in inventory:
        message = "Mặt hàng đã tồn tại ."
    else:
        inventory[name] = quantity
        message = f"Đã thêm {name} với số lượng {quantity} phần vào tồn ngày."
    return redirect(url_for('display_inventory', message=message))

@app.route('/remove', methods=['POST'])
def remove_item():
    name = request.form['name']
    if name in inventory:
        del inventory[name]
        message = f"Đã xóa {name} ."
    else:
        message = "Mặt hàng không tồn ngày."
    return redirect(url_for('display_inventory', message=message))

@app.route('/increase', methods=['POST'])
def increase_quantity():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    if name in inventory:
        inventory[name] += quantity
        message = f"Đã tăng {quantity} phần cho {name}. Số lượng hiện tại: {inventory[name]} phần."
    else:
        message = "Mặt hàng không tồn tại."
    return redirect(url_for('display_inventory', message=message))

@app.route('/decrease', methods=['POST'])
def decrease_quantity():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    if name in inventory:
        if inventory[name] >= quantity:
            inventory[name] -= quantity
            message = f"Đã giảm {quantity} phần từ {name}. Số lượng hiện tại: {inventory[name]} phần."
        else:
            message = "Không đủ số lượng để giảm."
    else:
        message = "Mặt hàng không tồn tại."
    return redirect(url_for('display_inventory', message=message))

@app.route('/adjust', methods=['POST'])
def adjust_quantity():
    name = request.form['name']
    adjustment = int(request.form['adjustment'])
    if name in inventory:
        new_quantity = inventory[name] + adjustment
        if new_quantity < 0:
            message = "Không đủ số lượng để giảm."
        else:
            inventory[name] = new_quantity
            message = f"Số lượng của {name} hiện tại: {inventory[name]} phần."
    else:
        message = "Mặt hàng không tồn tại."
    return redirect(url_for('display_inventory', message=message))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
