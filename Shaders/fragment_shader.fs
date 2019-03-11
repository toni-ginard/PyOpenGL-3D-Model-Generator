#version 330
in vec2 newTexture;
in vec3 fragNormal;

out vec4 outColor;
uniform sampler2D samplerTexture;

in vec3 fragPos; //
uniform vec3 lightPos; //

void main()
{
    vec3 ambient = vec3(1.0f, 0.2f, 0.4f) * 0.1f;

    vec3 sunLightIntensity = vec3(0.9f, 0.9f, 0.9f);
    vec3 sunLightDirection = normalize(vec3(2.0f, 2.0f, 0.0f));

    // outColor = vec4(0.8, 0.2, 0.0, 1.0);

    vec3 norm = normalize(fragNormal);
    vec3 lightDir = normalize(lightPos - fragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * vec3(0.0, 0.0, 0.0); //
    vec3 result = (ambient + diffuse) * vec3(1.0, 0.2, 0.0);
    outColor = vec4(result, 1.0);
}