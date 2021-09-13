# 快速入门文档，介绍一些常用的使用方式。
* [Gradle 构建语言参考](https://docs.gradle.org/current/dsl/index.html)
* [构建脚本基础](https://docs.gradle.org/current/userguide/tutorial_using_tasks.html)
* [开发自定义 Gradle 任务类型](https://docs.gradle.org/current/userguide/custom_tasks.html#custom_tasks)
* [Google 官方中文文档](https://developer.android.com/studio/build/gradle-tips?hl=zh-cn)
* [Android Gradle 中文文档](https://chaosleong.gitbooks.io/gradle-for-android/content/)

## 环境配置
* 这里直接采用 Android Studio 集成的 Gradle 插件.
* 在 build.gradle(:app)中直接输入学习的代码即可(可以先清空文件中的内容),不要点击 Sync Now
* 在底部找到 Terminal 面板，直接输入 gradlew
* 命令行会输出当前的 Gradle 版本信息
* 原命令 gradle 在 Android Studio 中被改成 gradlew
	```
	如:gradlew -q hello
	```

