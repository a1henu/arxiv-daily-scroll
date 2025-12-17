---
layout: default
title: Dual Attention Guided Defense Against Malicious Edits
---

# Dual Attention Guided Defense Against Malicious Edits
**arXiv**：[2512.14333v1](https://arxiv.org/abs/2512.14333) · [PDF](https://arxiv.org/pdf/2512.14333.pdf)  
**作者**：Jie Zhang, Shuai Dong, Shiguang Shan, Xilin Chen  

**一句话要点**：提出双注意力引导噪声扰动免疫方法以防御文本到图像扩散模型的恶意编辑

**关键词**：扩散模型防御, 注意力机制, 噪声扰动, 恶意编辑, 图像生成安全

## 3 点简述
- 核心问题：文本到图像扩散模型易被滥用生成欺骗性内容，现有防御方法对恶意篡改效果有限。
- 方法要点：通过多时间步操作，动态调整交叉注意力图和噪声预测，误导编辑至错误区域并保护目标。
- 实验或效果：在广泛实验中，该方法展现出对恶意编辑的强免疫力，达到最先进性能。

## 摘要（原文）

> Recent progress in text-to-image diffusion models has transformed image editing via text prompts, yet this also introduces significant ethical challenges from potential misuse in creating deceptive or harmful content. While current defenses seek to mitigate this risk by embedding imperceptible perturbations, their effectiveness is limited against malicious tampering. To address this issue, we propose a Dual Attention-Guided Noise Perturbation (DANP) immunization method that adds imperceptible perturbations to disrupt the model's semantic understanding and generation process. DANP functions over multiple timesteps to manipulate both cross-attention maps and the noise prediction process, using a dynamic threshold to generate masks that identify text-relevant and irrelevant regions. It then reduces attention in relevant areas while increasing it in irrelevant ones, thereby misguides the edit towards incorrect regions and preserves the intended targets. Additionally, our method maximizes the discrepancy between the injected noise and the model's predicted noise to further interfere with the generation. By targeting both attention and noise prediction mechanisms, DANP exhibits impressive immunity against malicious edits, and extensive experiments confirm that our method achieves state-of-the-art performance.

