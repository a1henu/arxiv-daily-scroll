---
layout: default
title: An Image Is Worth Ten Thousand Words: Verbose-Text Induction Attacks on VLMs
---

# An Image Is Worth Ten Thousand Words: Verbose-Text Induction Attacks on VLMs
**arXiv**：[2511.16163v1](https://arxiv.org/abs/2511.16163) · [PDF](https://arxiv.org/pdf/2511.16163.pdf)  
**作者**：Zhi Luo, Zenghui Yuan, Wenqi Wei, Daizong Liu, Pan Zhou  

**一句话要点**：提出冗长文本诱导攻击以优化视觉语言模型输出长度

**关键词**：视觉语言模型, 对抗攻击, 冗长文本生成, 扰动优化, 强化学习, 部署效率

## 3 点简述
- 核心问题：现有方法无法稳定最大化视觉语言模型输出令牌长度，影响部署效率。
- 方法要点：采用两阶段框架，结合对抗提示搜索和视觉对齐扰动优化。
- 实验效果：在四种流行模型上验证了方法在有效性和泛化性上的优势。

## 摘要（原文）

> With the remarkable success of Vision-Language Models (VLMs) on multimodal tasks, concerns regarding their deployment efficiency have become increasingly prominent. In particular, the number of tokens consumed during the generation process has emerged as a key evaluation metric.Prior studies have shown that specific inputs can induce VLMs to generate lengthy outputs with low information density, which significantly increases energy consumption, latency, and token costs. However, existing methods simply delay the occurrence of the EOS token to implicitly prolong output, and fail to directly maximize the output token length as an explicit optimization objective, lacking stability and controllability.To address these limitations, this paper proposes a novel verbose-text induction attack (VTIA) to inject imperceptible adversarial perturbations into benign images via a two-stage framework, which identifies the most malicious prompt embeddings for optimizing and maximizing the output token of the perturbed images.Specifically, we first perform adversarial prompt search, employing reinforcement learning strategies to automatically identify adversarial prompts capable of inducing the LLM component within VLMs to produce verbose outputs. We then conduct vision-aligned perturbation optimization to craft adversarial examples on input images, maximizing the similarity between the perturbed image's visual embeddings and those of the adversarial prompt, thereby constructing malicious images that trigger verbose text generation. Comprehensive experiments on four popular VLMs demonstrate that our method achieves significant advantages in terms of effectiveness, efficiency, and generalization capability.

