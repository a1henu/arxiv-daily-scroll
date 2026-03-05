---
layout: default
title: Tuning Just Enough: Lightweight Backdoor Attacks on Multi-Encoder Diffusion Models
---

# Tuning Just Enough: Lightweight Backdoor Attacks on Multi-Encoder Diffusion Models
**arXiv**：[2603.04064v1](https://arxiv.org/abs/2603.04064) · [PDF](https://arxiv.org/pdf/2603.04064.pdf)  
**作者**：Ziyuan Chen, Yujin Jeong, Tobias Braun, Anna Rohrbach  

**一句话要点**：提出MELT方法，针对多编码器扩散模型实现轻量级后门攻击

**关键词**：后门攻击, 多编码器扩散模型, 轻量级训练, 文本到图像生成, Stable Diffusion 3

## 3 点简述
- 研究多编码器扩散模型的后门攻击，聚焦Stable Diffusion 3的文本编码器漏洞
- 定义四类攻击目标，识别最小编码器集，提出仅训练低秩适配器的MELT方法
- 实验显示调整少于0.2%参数即可成功攻击，揭示多编码器场景下的新漏洞

## 摘要（原文）

> As text-to-image diffusion models become increasingly deployed in real-world applications, concerns about backdoor attacks have gained significant attention. Prior work on text-based backdoor attacks has largely focused on diffusion models conditioned on a single lightweight text encoder. However, more recent diffusion models that incorporate multiple large-scale text encoders remain underexplored in this context. Given the substantially increased number of trainable parameters introduced by multiple text encoders, an important question is whether backdoor attacks can remain both efficient and effective in such settings. In this work, we study Stable Diffusion 3, which uses three distinct text encoders and has not yet been systematically analyzed for text-encoder-based backdoor vulnerabilities. To understand the role of text encoders in backdoor attacks, we define four categories of attack targets and identify the minimal sets of encoders required to achieve effective performance for each attack objective. Based on this, we further propose Multi-Encoder Lightweight aTtacks (MELT), which trains only low-rank adapters while keeping the pretrained text encoder weight frozen. We demonstrate that tuning fewer than 0.2% of the total encoder parameters is sufficient for successful backdoor attacks on Stable Diffusion 3, revealing previously underexplored vulnerabilities in practical attack scenarios in multi-encoder settings.

