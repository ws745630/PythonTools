# Flutter入门

## Dart介绍

**var**:可以接收任何类型的变量，var 变量一旦赋值，类型便会确定，则不能再改变其类型

**dynamic**和**Object**:是 Dart 所有对象的根基类,`dynamic`与`Object`声明的变量都可以赋值任意对象，且后期可以改变赋值的类型；`dynamic`与`Object`不同的是`dynamic`声明的对象编译器会提供所有可能的组合，而`Object`声明的对象只能使用 `Object` 的属性与方法, 否则编译器会报错

**final**和**const**:常量，两者区别在于：const 变量是一个编译时常量（编译时直接替换为常量值），final变量在第一次使用时被初始化

## 常用命令

- `flutter create 项目名称 ` 创建flutter项目
- ` flutter run `运行flutter项目
-  `flutter devices` 查看可运行的设备列表
-  `flutter add pub 第三方库名称`或者修改`pubspec.yaml`文件的`dependencies`字段
-  `flutter packages get 第三方库名称`





