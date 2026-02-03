---
layout: default
title: LangMap: A Hierarchical Benchmark for Open-Vocabulary Goal Navigation
---

# LangMap: A Hierarchical Benchmark for Open-Vocabulary Goal Navigation
**arXiv**：[2602.02220v1](https://arxiv.org/abs/2602.02220) · [PDF](https://arxiv.org/pdf/2602.02220.pdf)  
**作者**：Bo Miao, Weijia Liu, Jun Luo, Lachlan Shinnick, Jian Liu, Thomas Hamilton-Smith, Yuhe Yang, Zijie Wu, Vanja Videnovic, Feras Dayoub, Anton van den Hengel  

**一句话要点**：提出LangMap基准以解决多粒度开放词汇目标导航任务，基于真实3D室内扫描构建。

**关键词**：开放词汇导航, 多粒度语义, 具身智能, 3D室内扫描, 语言驱动导航, 基准测试

## 3 点简述
- 核心问题：语言与对象关系对具身智能至关重要，需评估多粒度导航能力。
- 方法要点：构建LangMap基准，包含场景、房间、区域和实例四级语义目标，提供人类验证标注。
- 实验或效果：LangMap在判别准确率上优于GOAT-Bench 23.8%，评估显示上下文和记忆提升成功率，但长尾目标等仍具挑战。

## 摘要（原文）

> The relationships between objects and language are fundamental to meaningful communication between humans and AI, and to practically useful embodied intelligence. We introduce HieraNav, a multi-granularity, open-vocabulary goal navigation task where agents interpret natural language instructions to reach targets at four semantic levels: scene, room, region, and instance. To this end, we present Language as a Map (LangMap), a large-scale benchmark built on real-world 3D indoor scans with comprehensive human-verified annotations and tasks spanning these levels. LangMap provides region labels, discriminative region descriptions, discriminative instance descriptions covering 414 object categories, and over 18K navigation tasks. Each target features both concise and detailed descriptions, enabling evaluation across different instruction styles. LangMap achieves superior annotation quality, outperforming GOAT-Bench by 23.8% in discriminative accuracy using four times fewer words. Comprehensive evaluations of zero-shot and supervised models on LangMap reveal that richer context and memory improve success, while long-tailed, small, context-dependent, and distant goals, as well as multi-goal completion, remain challenging. HieraNav and LangMap establish a rigorous testbed for advancing language-driven embodied navigation. Project: https://bo-miao.github.io/LangMap

