---
layout: default
title: FaceRefiner: High-Fidelity Facial Texture Refinement with Differentiable Rendering-based Style Transfer
---

# FaceRefiner: High-Fidelity Facial Texture Refinement with Differentiable Rendering-based Style Transfer
**arXiv**：[2601.04520v1](https://arxiv.org/abs/2601.04520) · [PDF](https://arxiv.org/pdf/2601.04520.pdf)  
**作者**：Chengyang Li, Baoping Cheng, Yao Cheng, Haocheng Zhang, Renshuai Liu, Yinglin Zheng, Jing Liao, Xuan Cheng  

**一句话要点**：提出FaceRefiner，基于可微分渲染的风格迁移方法，以提升单图像生成面部纹理的保真度与身份一致性。

**关键词**：面部纹理生成, 风格迁移, 可微分渲染, 身份保持, 纹理细化

## 3 点简述
- 核心问题：现有方法从单图像生成面部纹理时，因训练数据或2D生成器限制，导致细节、结构和身份与输入不一致。
- 方法要点：将3D采样纹理作为风格，生成纹理作为内容，通过可微分渲染实现多级信息迁移，包括像素级细节。
- 实验或效果：在Multi-PIE、CelebA和FFHQ数据集上验证，能提升纹理质量和身份保持能力，优于现有技术。

## 摘要（原文）

> Recent facial texture generation methods prefer to use deep networks to synthesize image content and then fill in the UV map, thus generating a compelling full texture from a single image. Nevertheless, the synthesized texture UV map usually comes from a space constructed by the training data or the 2D face generator, which limits the methods' generalization ability for in-the-wild input images. Consequently, their facial details, structures and identity may not be consistent with the input. In this paper, we address this issue by proposing a style transfer-based facial texture refinement method named FaceRefiner. FaceRefiner treats the 3D sampled texture as style and the output of a texture generation method as content. The photo-realistic style is then expected to be transferred from the style image to the content image. Different from current style transfer methods that only transfer high and middle level information to the result, our style transfer method integrates differentiable rendering to also transfer low level (or pixel level) information in the visible face regions. The main benefit of such multi-level information transfer is that, the details, structures and semantics in the input can thus be well preserved. The extensive experiments on Multi-PIE, CelebA and FFHQ datasets demonstrate that our refinement method can improve the texture quality and the face identity preserving ability, compared with state-of-the-arts.

