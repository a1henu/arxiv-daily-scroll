---
layout: default
title: VidDoS: Universal Denial-of-Service Attack on Video-based Large Language Models
---

# VidDoS: Universal Denial-of-Service Attack on Video-based Large Language Models
**arXiv**：[2603.01454v1](https://arxiv.org/abs/2603.01454) · [PDF](https://arxiv.org/pdf/2603.01454.pdf)  
**作者**：Duoxun Tang, Dasen Dai, Jiyao Wang, Xiao Yang, Jianyu Wang, Siqi Cai  

**一句话要点**：提出VidDoS通用拒绝服务攻击框架，针对视频大语言模型在安全关键应用中的能量延迟攻击问题。

**关键词**：视频大语言模型, 拒绝服务攻击, 能量延迟攻击, 通用优化, 实时安全, 自动驾驶

## 3 点简述
- 核心问题：视频大语言模型易受能量延迟攻击，现有图像方法因时间聚合机制失效，实时优化不切实际。
- 方法要点：采用通用优化生成实例无关触发器，结合掩码教师强制、拒绝惩罚和提前终止抑制来引导模型生成高成本序列。
- 实验或效果：在三个主流模型和数据集上测试，导致令牌扩展超205倍、推理延迟增超15倍，模拟自动驾驶场景引发安全违规。

## 摘要（原文）

> Video-LLMs are increasingly deployed in safety-critical applications but are vulnerable to Energy-Latency Attacks (ELAs) that exhaust computational resources. Current image-centric methods fail because temporal aggregation mechanisms dilute individual frame perturbations. Additionally, real-time demands make instance-wise optimization impractical for continuous video streams. We introduce VidDoS, which is the first universal ELA framework tailored for Video-LLMs. Our method leverages universal optimization to create instance-agnostic triggers that require no inference-time gradient calculation. We achieve this through $\textit{masked teacher forcing}$ to steer models toward expensive target sequences, combined with a $\textit{refusal penalty}$ and $\textit{early-termination suppression}$ to override conciseness priors. Testing across three mainstream Video-LLMs and three video datasets, which include video question answering and autonomous driving scenarios, shows extreme degradation. VidDoS induces a token expansion of more than 205$\times$ and inflates the inference latency by more than 15$\times$ relative to clean baselines. Simulations of real-time autonomous driving streams further reveal that this induced latency leads to critical safety violations. We urge the community to recognize and mitigate these high-hazard ELA in Video-LLMs.

