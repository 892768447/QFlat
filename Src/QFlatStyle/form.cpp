#include "form.h"
#include "ui_form.h"
#include <QMenu>

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    QMenu *menu = new QMenu();
    menu->addAction("menu 1");
    menu->addAction("menu 2");
    menu->addAction("menu 3");
    menu->addAction("menu 4");
    ui->pushButtonMenu->setMenu(menu);
}

Form::~Form()
{
    delete ui;
}
