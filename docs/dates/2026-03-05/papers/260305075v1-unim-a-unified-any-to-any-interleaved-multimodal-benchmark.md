---
layout: default
title: UniM: A Unified Any-to-Any Interleaved Multimodal Benchmark
---

# UniM: A Unified Any-to-Any Interleaved Multimodal Benchmark
**arXiv**：[2603.05075v1](https://arxiv.org/abs/2603.05075) · [PDF](https://arxiv.org/pdf/2603.05075.pdf)  
**作者**：Yanlin Li, Minghui Guo, Kaiwen Zhang, Shize Zhang, Yiran Zhao, Haodong Li, Congyue Zhou, Weijie Zheng, Yushen Yan, Shengqiong Wu, Wei Ji, Lei Cui, Furu Wei, Hao Fei, Mong-Li Lee, Wynne Hsu  

**一句话要点**：提出UniM基准以评估任意模态交错输入输出的统一多模态学习能力

**关键词**：任意到任意多模态学习, 交错多模态基准, 多模态大语言模型评估, 统一理解与生成, 多模态数据集, 交错连贯性

## 3 点简述
- 核心问题：现实多模态应用需处理任意组合交错输入并生成任意交错输出，现有基准不足
- 方法要点：构建首个统一任意到任意交错多模态数据集，含31K实例覆盖7模态，并设计三维评估套件
- 实验或效果：基准难度高，突显统一多模态智能的关键挑战，提出可追溯推理的基线模型UniMA

## 摘要（原文）

> In real-world multimodal applications, systems usually need to comprehend arbitrarily combined and interleaved multimodal inputs from users, while also generating outputs in any interleaved multimedia form. This capability defines the goal of any-to-any interleaved multimodal learning under a unified paradigm of understanding and generation, posing new challenges and opportunities for advancing Multimodal Large Language Models (MLLMs). To foster and benchmark this capability, this paper introduces the UniM benchmark, the first Unified Any-to-Any Interleaved Multimodal dataset. UniM contains 31K high-quality instances across 30 domains and 7 representative modalities: text, image, audio, video, document, code, and 3D, each requiring multiple intertwined reasoning and generation capabilities. We further introduce the UniM Evaluation Suite, which assesses models along three dimensions: Semantic Correctness & Generation Quality, Response Structure Integrity, and Interleaved Coherence. In addition, we propose UniMA, an agentic baseline model equipped with traceable reasoning for structured interleaved generation. Comprehensive experiments demonstrate the difficulty of UniM and highlight key challenges and directions for advancing unified any-to-any multimodal intelligence. The project page is https://any2any-mllm.github.io/unim.

