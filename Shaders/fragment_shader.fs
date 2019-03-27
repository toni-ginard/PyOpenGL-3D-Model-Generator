#version 330

out vec4 outColor;

float near = 0.1;
float far  = 100.0;

float linearizeDepth(float depth)
{
    float z = depth * 2.0 - 1.0;
    return (2.0 * near) / (far + near - z * (far - near));
}

void main()
{
    float d = linearizeDepth(gl_FragCoord.z);
    outColor = vec4(vec3(d), 1.0);
}