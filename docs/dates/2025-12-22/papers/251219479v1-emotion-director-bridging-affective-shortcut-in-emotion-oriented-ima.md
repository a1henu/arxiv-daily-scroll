---
layout: default
title: Emotion-Director: Bridging Affective Shortcut in Emotion-Oriented Image Generation
---

# Emotion-Director: Bridging Affective Shortcut in Emotion-Oriented Image Generation
**arXiv**：[2512.19479v1](https://arxiv.org/abs/2512.19479) · [PDF](https://arxiv.org/pdf/2512.19479.pdf)  
**作者**：Guoli Jia, Junyao Hu, Xinwei Long, Kai Tian, Kaiyan Zhang, KaiKai Zhao, Ning Ding, Bowen Zhou  

**一句话要点**：提出Emotion-Director框架以解决情感导向图像生成中的情感捷径问题

**关键词**：情感导向图像生成, 扩散模型, 跨模态协作, 情感捷径, 提示改写, 多智能体系统

## 3 点简述
- 核心问题：现有方法将情感近似为语义，导致情感捷径，忽略情感与语义的差异
- 方法要点：结合MC-Diffusion模型和MC-Agent系统，通过跨模态协作生成超越语义的情感导向图像
- 实验或效果：定性和定量实验显示Emotion-Director在情感导向图像生成中表现优越

## 摘要（原文）

> Image generation based on diffusion models has demonstrated impressive capability, motivating exploration into diverse and specialized applications. Owing to the importance of emotion in advertising, emotion-oriented image generation has attracted increasing attention. However, current emotion-oriented methods suffer from an affective shortcut, where emotions are approximated to semantics. As evidenced by two decades of research, emotion is not equivalent to semantics. To this end, we propose Emotion-Director, a cross-modal collaboration framework consisting of two modules. First, we propose a cross-Modal Collaborative diffusion model, abbreviated as MC-Diffusion. MC-Diffusion integrates visual prompts with textual prompts for guidance, enabling the generation of emotion-oriented images beyond semantics. Further, we improve the DPO optimization by a negative visual prompt, enhancing the model's sensitivity to different emotions under the same semantics. Second, we propose MC-Agent, a cross-Modal Collaborative Agent system that rewrites textual prompts to express the intended emotions. To avoid template-like rewrites, MC-Agent employs multi-agents to simulate human subjectivity toward emotions, and adopts a chain-of-concept workflow that improves the visual expressiveness of the rewritten prompts. Extensive qualitative and quantitative experiments demonstrate the superiority of Emotion-Director in emotion-oriented image generation.

