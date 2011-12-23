function ItemsList(id) {
    this.id = id;
    this.items = [];
    this.cursor = 0;
}

ItemsList.prototype.load_items_list = function() {
    var list = []
    $("#" + this.id + " > li").each(function () {
        list.push($(this));
    });
    this.items = list;
};

ItemsList.prototype.show_items = function() {
    var left_bound = this.cursor;
    var right_bound = this.cursor + 4;
    for (var i = 0; i < this.items.length; i++) {
        if ((i > right_bound) || (i < left_bound)) {
            this.items[i].hide('slow');
        }
        else
        {
            this.items[i].show('slow');
        }
    }
};

ItemsList.prototype.set_up_list = function() {
    this.load_items_list();
    var item_height = this.items[0].height();
    $("#" + this.id).height(item_height);
    this.show_items();
}

ItemsList.prototype.move_right = function() {
    if (this.cursor < (this.items.length-5)) {
        this.cursor = this.cursor + 1;
        this.show_items();
    }

};

ItemsList.prototype.move_left = function() {
    if (this.cursor > 0) {
        this.cursor = this.cursor - 1;
        this.show_items();
    }
};


