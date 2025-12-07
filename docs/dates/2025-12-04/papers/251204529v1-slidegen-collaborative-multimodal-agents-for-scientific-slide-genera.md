---
layout: default
title: SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation
---

# SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation
**arXiv**：[2512.04529v1](https://arxiv.org/abs/2512.04529) · [PDF](https://arxiv.org/pdf/2512.04529.pdf)  
**作者**：Xin Liang, Xiang Zhang, Yiwei Xu, Siqi Sun, Chenyu You  

**一句话要点**：提出SlideGen框架，通过多智能体协作解决科学论文到演示文稿的生成问题。

**关键词**：多模态推理, 智能体协作, 幻灯片生成, 视觉规划, 文档理解

## 3 点简述
- 核心问题：现有方法忽视视觉规划，难以生成高质量学术幻灯片。
- 方法要点：采用模块化多智能体框架，协同处理文档结构与视觉设计。
- 实验或效果：在多个基准测试中，SlideGen在视觉质量、内容忠实度和可读性上优于现有方法。

## 摘要（原文）

> Generating academic slides from scientific papers is a challenging multimodal reasoning task that requires both long context understanding and deliberate visual planning. Existing approaches largely reduce it to text only summarization, overlooking the visual component and design intensive nature of slide creation. In this paper we introduce SlideGen, an agentic, modular, and visual in the loop framework for scientific paper to slide generation. SlideGen orchestrates a group of vision language agents that reason collaboratively over the document structure and semantics, producing editable PPTX slides with logical flow and compelling visual presentation. By integrating coordinated outlining, mapping, arrangement, note synthesis, and iterative refinement, our system consistently delivers slides of expert level quality. Across diverse benchmarks and strong baselines, SlideGen outperforms existing methods in visual quality, content faithfulness, and readability, positioning it as the new state of the art in automated slide generation. Our work establishes a foundation for design aware multimodal slide generation, demonstrating how agentic collaboration can bridge understanding and presentation in complex multimodal reasoning tasks.

