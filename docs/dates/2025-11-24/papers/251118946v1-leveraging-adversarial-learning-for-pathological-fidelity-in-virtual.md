---
layout: default
title: Leveraging Adversarial Learning for Pathological Fidelity in Virtual Staining
---

# Leveraging Adversarial Learning for Pathological Fidelity in Virtual Staining
**arXiv**：[2511.18946v1](https://arxiv.org/abs/2511.18946) · [PDF](https://arxiv.org/pdf/2511.18946.pdf)  
**作者**：José Teixeira, Pascal Klöckner, Diana Montezuma, Melis Erdal Cesur, João Fraga, Hugo M. Horlings, Jaime S. Cardoso, Sara P. Oliveira  

**一句话要点**：提出CSSP2P GAN以提升虚拟染色病理保真度

**关键词**：虚拟染色, 生成对抗网络, 病理保真度, 图像翻译, 对抗损失, 模型评估

## 3 点简述
- 虚拟染色可替代昂贵免疫组化，但现有方法忽略对抗损失影响
- 开发CSSP2P GAN，通过对抗学习增强病理保真度
- 盲法专家评估显示模型优于现有方法，并揭示指标局限性

## 摘要（原文）

> In addition to evaluating tumor morphology using H&E staining, immunohistochemistry is used to assess the presence of specific proteins within the tissue. However, this is a costly and labor-intensive technique, for which virtual staining, as an image-to-image translation task, offers a promising alternative. Although recent, this is an emerging field of research with 64% of published studies just in 2024. Most studies use publicly available datasets of H&E-IHC pairs from consecutive tissue sections. Recognizing the training challenges, many authors develop complex virtual staining models based on conditional Generative Adversarial Networks, but ignore the impact of adversarial loss on the quality of virtual staining. Furthermore, overlooking the issues of model evaluation, they claim improved performance based on metrics such as SSIM and PSNR, which are not sufficiently robust to evaluate the quality of virtually stained images. In this paper, we developed CSSP2P GAN, which we demonstrate to achieve heightened pathological fidelity through a blind pathological expert evaluation. Furthermore, while iteratively developing our model, we study the impact of the adversarial loss and demonstrate its crucial role in the quality of virtually stained images. Finally, while comparing our model with reference works in the field, we underscore the limitations of the currently used evaluation metrics and demonstrate the superior performance of CSSP2P GAN.

