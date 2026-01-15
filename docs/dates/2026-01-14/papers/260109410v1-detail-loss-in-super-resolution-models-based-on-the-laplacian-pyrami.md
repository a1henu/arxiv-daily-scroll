---
layout: default
title: Detail Loss in Super-Resolution Models Based on the Laplacian Pyramid and Repeated Upscaling and Downscaling Process
---

# Detail Loss in Super-Resolution Models Based on the Laplacian Pyramid and Repeated Upscaling and Downscaling Process
**arXiv**：[2601.09410v1](https://arxiv.org/abs/2601.09410) · [PDF](https://arxiv.org/pdf/2601.09410.pdf)  
**作者**：Sangjun Han, Youngmi Hur  

**一句话要点**：提出基于拉普拉斯金字塔的细节损失和重复上下采样过程，以增强超分辨率图像的高频细节。

**关键词**：图像超分辨率, 细节损失, 拉普拉斯金字塔, 重复上下采样, 高频增强, CNN模型

## 3 点简述
- 核心问题：超分辨率任务中高频细节增强不足，影响图像质量。
- 方法要点：使用拉普拉斯金字塔损失分离控制超分辨率和细节图像，结合重复上下采样提取多尺度特征。
- 实验或效果：在CNN和注意力模型中均提升性能，CNN模型达到SOTA，注意力模型改进原版。

## 摘要（原文）

> With advances in artificial intelligence, image processing has gained significant interest. Image super-resolution is a vital technology closely related to real-world applications, as it enhances the quality of existing images. Since enhancing fine details is crucial for the super-resolution task, pixels that contribute to high-frequency information should be emphasized. This paper proposes two methods to enhance high-frequency details in super-resolution images: a Laplacian pyramid-based detail loss and a repeated upscaling and downscaling process. Total loss with our detail loss guides a model by separately generating and controlling super-resolution and detail images. This approach allows the model to focus more effectively on high-frequency components, resulting in improved super-resolution images. Additionally, repeated upscaling and downscaling amplify the effectiveness of the detail loss by extracting diverse information from multiple low-resolution features. We conduct two types of experiments. First, we design a CNN-based model incorporating our methods. This model achieves state-of-the-art results, surpassing all currently available CNN-based and even some attention-based models. Second, we apply our methods to existing attention-based models on a small scale. In all our experiments, attention-based models adding our detail loss show improvements compared to the originals. These results demonstrate our approaches effectively enhance super-resolution images across different model structures.

