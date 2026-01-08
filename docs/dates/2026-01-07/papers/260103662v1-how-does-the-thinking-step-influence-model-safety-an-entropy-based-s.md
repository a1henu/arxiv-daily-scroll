---
layout: default
title: How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs
---

# How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs
**arXiv**：[2601.03662v1](https://arxiv.org/abs/2601.03662) · [PDF](https://arxiv.org/pdf/2601.03662.pdf)  
**作者**：Su-Hyeon Kim, Hyundong Jin, Yejin Lee, Yo-Sub Han  

**一句话要点**：提出SafeRemind以解决大型推理模型思考步骤中的安全风险

**关键词**：大型推理模型, 模型安全, 解码时防御, 熵触发, 安全提醒

## 3 点简述
- 核心问题：大型推理模型的思考步骤可能放大不安全行为，传统防御机制无效
- 方法要点：基于熵触发动态注入安全提醒短语，无需参数更新
- 实验或效果：在五个模型和六个基准上提升安全性达45.5%，保持推理效用

## 摘要（原文）

> Large Reasoning Models (LRMs) achieve remarkable success through explicit thinking steps, yet the thinking steps introduce a novel risk by potentially amplifying unsafe behaviors. Despite this vulnerability, conventional defense mechanisms remain ineffective as they overlook the unique reasoning dynamics of LRMs. In this work, we find that the emergence of safe-reminding phrases within thinking steps plays a pivotal role in ensuring LRM safety. Motivated by this finding, we propose SafeRemind, a decoding-time defense method that dynamically injects safe-reminding phrases into thinking steps. By leveraging entropy triggers to intervene at decision-locking points, SafeRemind redirects potentially harmful trajectories toward safer outcomes without requiring any parameter updates. Extensive evaluations across five LRMs and six benchmarks demonstrate that SafeRemind substantially enhances safety, achieving improvements of up to 45.5%p while preserving core reasoning utility.

