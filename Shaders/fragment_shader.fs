#version 330
out vec4 outColor;
in vec2 newTexture;
uniform sampler2D samplerTexture;
void main()
{
    outColor = texture(samplerTexture, newTexture);
}