---
layout: default
title: UniGenBench++: A Unified Semantic Evaluation Benchmark for Text-to-Image Generation
---

# UniGenBench++: A Unified Semantic Evaluation Benchmark for Text-to-Image Generation
**arXiv**：[2510.18701v1](https://arxiv.org/abs/2510.18701) · [PDF](https://arxiv.org/pdf/2510.18701.pdf)  
**作者**：Yibin Wang, Zhimin Li, Yuhang Zang, Jiazi Bu, Yujie Zhou, Yi Xin, Junjun He, Chunyu Wang, Qinglin Lu, Cheng Jin, Jiaqi Wang  

**一句话要点**：提出UniGenBench++统一基准，解决文本到图像生成语义评估的多样性和细粒度不足问题。

**关键词**：文本到图像生成, 语义评估基准, 多模态大语言模型, 多语言提示, 细粒度评估, 离线评估模型

## 3 点简述
- 现有基准缺乏多语言支持和多样化提示场景，影响实际应用。
- 构建600个提示，覆盖5主题20子主题，评估10主27子标准，使用MLLM自动评估。
- 通过中英文长短提示测试模型鲁棒性，并训练离线评估模型，系统揭示模型优缺点。

## 摘要（原文）

> Recent progress in text-to-image (T2I) generation underscores the importance
> of reliable benchmarks in evaluating how accurately generated images reflect
> the semantics of their textual prompt. However, (1) existing benchmarks lack
> the diversity of prompt scenarios and multilingual support, both essential for
> real-world applicability; (2) they offer only coarse evaluations across primary
> dimensions, covering a narrow range of sub-dimensions, and fall short in
> fine-grained sub-dimension assessment. To address these limitations, we
> introduce UniGenBench++, a unified semantic assessment benchmark for T2I
> generation. Specifically, it comprises 600 prompts organized hierarchically to
> ensure both coverage and efficiency: (1) spans across diverse real-world
> scenarios, i.e., 5 main prompt themes and 20 subthemes; (2) comprehensively
> probes T2I models' semantic consistency over 10 primary and 27 sub evaluation
> criteria, with each prompt assessing multiple testpoints. To rigorously assess
> model robustness to variations in language and prompt length, we provide both
> English and Chinese versions of each prompt in short and long forms. Leveraging
> the general world knowledge and fine-grained image understanding capabilities
> of a closed-source Multi-modal Large Language Model (MLLM), i.e.,
> Gemini-2.5-Pro, an effective pipeline is developed for reliable benchmark
> construction and streamlined model assessment. Moreover, to further facilitate
> community use, we train a robust evaluation model that enables offline
> assessment of T2I model outputs. Through comprehensive benchmarking of both
> open- and closed-sourced T2I models, we systematically reveal their strengths
> and weaknesses across various aspects.

