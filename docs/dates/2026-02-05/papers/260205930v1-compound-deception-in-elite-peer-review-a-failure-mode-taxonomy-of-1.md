---
layout: default
title: Compound Deception in Elite Peer Review: A Failure Mode Taxonomy of 100 Fabricated Citations at NeurIPS 2025
---

# Compound Deception in Elite Peer Review: A Failure Mode Taxonomy of 100 Fabricated Citations at NeurIPS 2025
**arXiv**：[2602.05930v1](https://arxiv.org/abs/2602.05930) · [PDF](https://arxiv.org/pdf/2602.05930.pdf)  
**作者**：Samar Ansari  

**一句话要点**：提出五类幻觉分类法以分析NeurIPS 2025中100个AI生成伪造引用的复合欺骗模式

**关键词**：伪造引用检测, 同行评审失败, AI幻觉分类, 学术诚信, 自动验证

## 3 点简述
- 核心问题：LLMs在学术写作中生成不存在的伪造引用，在NeurIPS 2025的53篇论文中逃过同行评审
- 方法要点：基于100个伪造引用开发五类失败模式分类法，揭示所有幻觉均呈现复合结构
- 实验或效果：发现92%受污染论文含1-2个幻觉，8%含4-13个，建议提交时强制自动验证

## 摘要（原文）

> Large language models (LLMs) are increasingly used in academic writing workflows, yet they frequently hallucinate by generating citations to sources that do not exist. This study analyzes 100 AI-generated hallucinated citations that appeared in papers accepted by the 2025 Conference on Neural Information Processing Systems (NeurIPS), one of the world's most prestigious AI conferences. Despite review by 3-5 expert researchers per paper, these fabricated citations evaded detection, appearing in 53 published papers (approx. 1% of all accepted papers). We develop a five-category taxonomy that classifies hallucinations by their failure mode: Total Fabrication (66%), Partial Attribute Corruption (27%), Identifier Hijacking (4%), Placeholder Hallucination (2%), and Semantic Hallucination (1%). Our analysis reveals a critical finding: every hallucination (100%) exhibited compound failure modes. The distribution of secondary characteristics was dominated by Semantic Hallucination (63%) and Identifier Hijacking (29%), which often appeared alongside Total Fabrication to create a veneer of plausibility and false verifiability. These compound structures exploit multiple verification heuristics simultaneously, explaining why peer review fails to detect them. The distribution exhibits a bimodal pattern: 92% of contaminated papers contain 1-2 hallucinations (minimal AI use) while 8% contain 4-13 hallucinations (heavy reliance). These findings demonstrate that current peer review processes do not include effective citation verification and that the problem extends beyond NeurIPS to other major conferences, government reports, and professional consulting. We propose mandatory automated citation verification at submission as an implementable solution to prevent fabricated citations from becoming normalized in scientific literature.

