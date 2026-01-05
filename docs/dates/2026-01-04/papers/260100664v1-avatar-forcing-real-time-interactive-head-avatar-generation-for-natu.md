---
layout: default
title: Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation
---

# Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation
**arXiv**：[2601.00664v1](https://arxiv.org/abs/2601.00664) · [PDF](https://arxiv.org/pdf/2601.00664.pdf)  
**作者**：Taekyung Ki, Sangwon Jang, Jaehyeong Jo, Jaehong Yoon, Sung Ju Hwang  

**一句话要点**：提出Avatar Forcing框架，通过扩散强制建模实时用户-头像交互，以解决虚拟对话中头像生成缺乏互动性和情感表达的问题。

**关键词**：说话头像生成, 实时交互, 扩散模型, 多模态输入, 直接偏好优化, 低延迟响应

## 3 点简述
- 核心问题：现有说话头像生成模型在实时交互中缺乏情感参与，难以处理因果约束下的实时运动生成。
- 方法要点：采用扩散强制技术处理多模态输入，实现低延迟响应；引入基于合成失败样本的直接偏好优化，无需额外标注数据学习表达性交互。
- 实验或效果：框架实现约500ms低延迟交互，比基线加速6.8倍，生成的反应性和表达性头像运动在偏好测试中超过80%优于基线。

## 摘要（原文）

> Talking head generation creates lifelike avatars from static portraits for virtual communication and content creation. However, current models do not yet convey the feeling of truly interactive communication, often generating one-way responses that lack emotional engagement. We identify two key challenges toward truly interactive avatars: generating motion in real-time under causal constraints and learning expressive, vibrant reactions without additional labeled data. To address these challenges, we propose Avatar Forcing, a new framework for interactive head avatar generation that models real-time user-avatar interactions through diffusion forcing. This design allows the avatar to process real-time multimodal inputs, including the user's audio and motion, with low latency for instant reactions to both verbal and non-verbal cues such as speech, nods, and laughter. Furthermore, we introduce a direct preference optimization method that leverages synthetic losing samples constructed by dropping user conditions, enabling label-free learning of expressive interaction. Experimental results demonstrate that our framework enables real-time interaction with low latency (approximately 500ms), achieving 6.8X speedup compared to the baseline, and produces reactive and expressive avatar motion, which is preferred over 80% against the baseline.

