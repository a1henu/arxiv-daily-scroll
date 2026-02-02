---
layout: default
title: PaperBanana: Automating Academic Illustration for AI Scientists
---

# PaperBanana: Automating Academic Illustration for AI Scientists
**arXiv**：[2601.23265v1](https://arxiv.org/abs/2601.23265) · [PDF](https://arxiv.org/pdf/2601.23265.pdf)  
**作者**：Dawei Zhu, Rui Meng, Yale Song, Xiyu Wei, Sujian Li, Tomas Pfister, Jinsung Yoon  

**一句话要点**：提出PaperBanana框架以自动化生成学术论文插图，减轻研究流程负担。

**关键词**：学术插图生成, 代理框架, 视觉语言模型, 图像生成, 自动化研究工具, 基准测试

## 3 点简述
- 核心问题：AI科学家研究中，生成出版级插图仍依赖人工，效率低下。
- 方法要点：基于先进视觉语言模型和图像生成模型，通过代理协作实现插图检索、规划、渲染和迭代优化。
- 实验或效果：在PaperBananaBench基准测试中，在忠实度、简洁性、可读性和美观性上优于基线，并扩展至统计图表生成。

## 摘要（原文）

> Despite rapid advances in autonomous AI scientists powered by language models, generating publication-ready illustrations remains a labor-intensive bottleneck in the research workflow. To lift this burden, we introduce PaperBanana, an agentic framework for automated generation of publication-ready academic illustrations. Powered by state-of-the-art VLMs and image generation models, PaperBanana orchestrates specialized agents to retrieve references, plan content and style, render images, and iteratively refine via self-critique. To rigorously evaluate our framework, we introduce PaperBananaBench, comprising 292 test cases for methodology diagrams curated from NeurIPS 2025 publications, covering diverse research domains and illustration styles. Comprehensive experiments demonstrate that PaperBanana consistently outperforms leading baselines in faithfulness, conciseness, readability, and aesthetics. We further show that our method effectively extends to the generation of high-quality statistical plots. Collectively, PaperBanana paves the way for the automated generation of publication-ready illustrations.

