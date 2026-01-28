---
layout: default
title: VC-Bench: Pioneering the Video Connecting Benchmark with a Dataset and Evaluation Metrics
---

# VC-Bench: Pioneering the Video Connecting Benchmark with a Dataset and Evaluation Metrics
**arXiv**：[2601.19236v1](https://arxiv.org/abs/2601.19236) · [PDF](https://arxiv.org/pdf/2601.19236.pdf)  
**作者**：Zhiyu Yin, Zhipeng Liu, Kehai Chen, Lemao Liu, Jin Liu, Hong-Dong Li, Yang Xiang, Min Zhang  

**一句话要点**：提出VC-Bench基准以解决视频连接任务中缺乏标准化评估的问题

**关键词**：视频连接, 评估基准, 视频生成, 数据集, 过渡平滑性, 起始-结束一致性

## 3 点简述
- 核心问题：视频连接任务缺乏标准化评估基准，阻碍了发展
- 方法要点：构建包含1,579个高质量视频的数据集，覆盖15个主类别和72个子类别
- 实验或效果：评估多个先进模型，发现其在保持起始-结束一致性和过渡平滑性方面存在显著局限

## 摘要（原文）

> While current video generation focuses on text or image conditions, practical applications like video editing and vlogging often need to seamlessly connect separate clips. In our work, we introduce Video Connecting, an innovative task that aims to generate smooth intermediate video content between given start and end clips. However, the absence of standardized evaluation benchmarks has hindered the development of this task. To bridge this gap, we proposed VC-Bench, a novel benchmark specifically designed for video connecting. It includes 1,579 high-quality videos collected from public platforms, covering 15 main categories and 72 subcategories to ensure diversity and structure. VC-Bench focuses on three core aspects: Video Quality Score VQS, Start-End Consistency Score SECS, and Transition Smoothness Score TSS. Together, they form a comprehensive framework that moves beyond conventional quality-only metrics. We evaluated multiple state-of-the-art video generation models on VC-Bench. Experimental results reveal significant limitations in maintaining start-end consistency and transition smoothness, leading to lower overall coherence and fluidity. We expect that VC-Bench will serve as a pioneering benchmark to inspire and guide future research in video connecting. The evaluation metrics and dataset are publicly available at: https://anonymous.4open.science/r/VC-Bench-1B67/.

