---
layout: default
title: WeMMU: Enhanced Bridging of Vision-Language Models and Diffusion Models via Noisy Query Tokens
---

# WeMMU: Enhanced Bridging of Vision-Language Models and Diffusion Models via Noisy Query Tokens
**arXiv**：[2512.02536v1](https://arxiv.org/abs/2512.02536) · [PDF](https://arxiv.org/pdf/2512.02536.pdf)  
**作者**：Jian Yang, Dacheng Yin, Xiaoxuan He, Yong Li, Fengyun Rao, Jing Lyu, Wei Zhai, Yang Cao, Zheng-Jun Zha  

**一句话要点**：提出Noisy Query Tokens以解决视觉语言模型与扩散模型桥接中的泛化崩溃问题

**关键词**：视觉语言模型, 扩散模型, 桥接方法, 持续学习, 图像生成

## 3 点简述
- 核心问题：固定查询令牌方法在桥接视觉语言模型与扩散模型时，面临任务泛化崩溃，难以适应新任务。
- 方法要点：引入Noisy Query Tokens，通过端到端优化学习分布式表示空间，并添加VAE分支以恢复图像细节。
- 实验或效果：实验证实该方法缓解泛化崩溃，支持跨任务的稳定持续学习。

## 摘要（原文）

> Recent progress in multimodal large language models (MLLMs) has highlighted the challenge of efficiently bridging pre-trained Vision-Language Models (VLMs) with Diffusion Models. While methods using a fixed number of learnable query tokens offer computational efficiency, they suffer from task generalization collapse, failing to adapt to new tasks that are distant from their pre-training tasks. To overcome this, we propose Noisy Query Tokens, which learn a distributed representation space between the VLM and Diffusion Model via end-to-end optimization, enhancing continual learning. Additionally, we introduce a VAE branch with linear projection to recover fine-grained image details. Experimental results confirm our approach mitigates generalization collapse and enables stable continual learning across diverse tasks.

