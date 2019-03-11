#version 330
in vec2 newTexture;
in vec3 fragNormal;
in vec3 fragPos;

out vec4 outColor;

void main()
{
    vec3 lightColor = vec3(1.0f, 1.0f, 1.0f);
    vec3 lightPos = vec3(1.2, 1.0, 2.0);
    vec3 objectColor = vec3(1.0f, 0.5f, 0.31f);

    vec3 ambient = lightColor * 0.1f; // ambientStrength

    vec3 norm = normalize(fragNormal);
    vec3 lightDir = normalize(lightPos - fragPos);

    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    vec3 result = (ambient + diffuse) * objectColor;

    outColor = vec4(result, 1.0);
}