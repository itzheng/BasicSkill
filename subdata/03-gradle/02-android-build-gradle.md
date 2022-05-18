# [build apk output name :](https://developer.android.com/studio/build/configure-apk-splits)
'''
// For each APK output variant, override versionCode with a combination of
// ext.abiCodes * 1000 + variant.versionCode. In this example, variant.versionCode
// is equal to defaultConfig.versionCode. If you configure product flavors that
// define their own versionCode, variant.versionCode uses that value instead.
android.applicationVariants.all { variant ->

    // Assigns a different version code for each output APK
    // other than the universal APK.
    variant.outputs.each { output ->
        print("output:"+output+"\n")
//        ApkVariantOutputImpl_Decorated
//        {variantOutput=VariantOutputImpl(
//        versionCode=property(java.lang.Integer, provider(class java.lang.Integer)), 
//        versionName=property(java.lang.String, provider(class java.lang.String)), 
//        enabled=property(java.lang.Boolean, fixed(class java.lang.Boolean, true)), 
//        variantOutputConfiguration=VariantOutputConfigurationImpl(isUniversal=false, filters=[]), 
//        baseName=debug, fullName=debug, 
//        outputFileName=property(java.lang.String, fixed(class java.lang.String, app-debug.apk))
//        )}
        def date = new Date().format("yyyyMMdd_HHmmss" , TimeZone.getTimeZone("GMT+08"))
        output. outputFileName = "${applicationId}_${versionName}_${variant.buildType.name}_${date}.apk"
    }
'''