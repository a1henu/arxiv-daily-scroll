---
layout: default
title: AVFakeBench: A Comprehensive Audio-Video Forgery Detection Benchmark for AV-LMMs
---

# AVFakeBench: A Comprehensive Audio-Video Forgery Detection Benchmark for AV-LMMs
**arXiv**：[2511.21251v1](https://arxiv.org/abs/2511.21251) · [PDF](https://arxiv.org/pdf/2511.21251.pdf)  
**作者**：Shuhan Xia, Peipei Li, Xuannan Liu, Dongsen Zhang, Xinyu Guo, Zekun Li  

**一句话要点**：提出AVFakeBench基准以解决音视频伪造检测多样性不足问题

**关键词**：音视频伪造检测, 多任务评估, 大语言模型, 伪造类型分类, 细粒度感知

## 3 点简述
- 核心问题：现有基准局限于DeepFake伪造，无法覆盖真实场景多样性
- 方法要点：构建多阶段混合伪造框架，集成专有模型与生成模型
- 实验或效果：评估11个AV-LMMs，揭示其在细粒度感知与推理中的弱点

## 摘要（原文）

> The threat of Audio-Video (AV) forgery is rapidly evolving beyond human-centric deepfakes to include more diverse manipulations across complex natural scenes. However, existing benchmarks are still confined to DeepFake-based forgeries and single-granularity annotations, thus failing to capture the diversity and complexity of real-world forgery scenarios. To address this, we introduce AVFakeBench, the first comprehensive audio-video forgery detection benchmark that spans rich forgery semantics across both human subject and general subject. AVFakeBench comprises 12K carefully curated audio-video questions, covering seven forgery types and four levels of annotations. To ensure high-quality and diverse forgeries, we propose a multi-stage hybrid forgery framework that integrates proprietary models for task planning with expert generative models for precise manipulation. The benchmark establishes a multi-task evaluation framework covering binary judgment, forgery types classification, forgery detail selection, and explanatory reasoning. We evaluate 11 Audio-Video Large Language Models (AV-LMMs) and 2 prevalent detection methods on AVFakeBench, demonstrating the potential of AV-LMMs as emerging forgery detectors while revealing their notable weaknesses in fine-grained perception and reasoning.

