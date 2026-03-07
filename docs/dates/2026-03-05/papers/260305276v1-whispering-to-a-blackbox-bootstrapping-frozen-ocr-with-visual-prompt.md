---
layout: default
title: Whispering to a Blackbox: Bootstrapping Frozen OCR with Visual Prompts
---

# Whispering to a Blackbox: Bootstrapping Frozen OCR with Visual Prompts
**arXiv**：[2603.05276v1](https://arxiv.org/abs/2603.05276) · [PDF](https://arxiv.org/pdf/2603.05276.pdf)  
**作者**：Samandar Samandarov, Nazirjon Ismoiljonov, Abdullah Sattorov, Temirlan Sabyrbayev  

**一句话要点**：提出视觉提示框架Whisperer，通过扩散模型预处理输入以提升冻结OCR性能

**关键词**：视觉提示, 扩散模型, 行为克隆, OCR增强, 冻结模型适配

## 3 点简述
- 核心问题：冻结预训练模型在特定任务上因数据分布不匹配而表现不佳
- 方法要点：采用行为克隆学习扩散模型预处理器，在像素空间优化输入
- 实验或效果：在30万张退化合成文本图像上，字符错误率降低8%（相对10.6%）

## 摘要（原文）

> In the landscape of modern machine learning, frozen pre-trained models provide stability and efficiency but often underperform on specific tasks due to mismatched data distributions. This paper introduces the Whisperer, a novel visual prompting framework that learns diffusion-based preprocessors to adapt inputs in pixel space, effectively "whispering" enhancements to frozen downstream models like EasyOCR. By framing the process as behavioral cloning of stochastically discovered improvement policies, our method achieves an 8% absolute (10.6% relative) reduction in Character Error Rate (CER) on a challenging dataset of 300k degraded synthetic text images, surpassing hand-engineered baselines such as CLAHE. The key innovation is a four-stage training curriculum that uses behavioral cloning to amplify "lucky" improvements discovered through the stochastic exploration of a partially trained diffusion model. This approach is highly sample-efficient and avoids the pitfalls of traditional reinforcement learning. Crucially, we frame this not as naive reinforcement learning, but as behavioral cloning of an exploration policy: we stochastically sample intermediate diffusion outputs, select those that improve CER by chance, and then train the model to reproduce them. This bootstrapping curriculum (4 stages over 60 GPU-hours) amplifies random successes into a systematic strategy. In summary, by whispering to the frozen OCR through its inputs, we improve an imperfect classifier without touching its weights.

