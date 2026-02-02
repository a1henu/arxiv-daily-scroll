---
layout: default
title: Procedural Knowledge Extraction from Industrial Troubleshooting Guides Using Vision Language Models
---

# Procedural Knowledge Extraction from Industrial Troubleshooting Guides Using Vision Language Models
**arXiv**：[2601.22754v1](https://arxiv.org/abs/2601.22754) · [PDF](https://arxiv.org/pdf/2601.22754.pdf)  
**作者**：Guillermo Gil de Avalle, Laura Maruster, Christos Emmanouilidis  

**一句话要点**：评估视觉语言模型从工业故障排除指南中提取结构化知识，比较两种提示策略。

**关键词**：视觉语言模型, 知识提取, 工业故障排除, 流程图解析, 提示策略

## 3 点简述
- 核心问题：工业故障排除指南以流程图形式编码诊断程序，手动提取知识耗时且易错。
- 方法要点：使用视觉语言模型联合解释视觉和文本信息，比较标准指令引导与增强布局提示策略。
- 实验或效果：结果揭示模型在布局敏感性和语义鲁棒性间的权衡，为实际部署提供参考。

## 摘要（原文）

> Industrial troubleshooting guides encode diagnostic procedures in flowchart-like diagrams where spatial layout and technical language jointly convey meaning. To integrate this knowledge into operator support systems, which assist shop-floor personnel in diagnosing and resolving equipment issues, the information must first be extracted and structured for machine interpretation. However, when performed manually, this extraction is labor-intensive and error-prone. Vision Language Models offer potential to automate this process by jointly interpreting visual and textual meaning, yet their performance on such guides remains underexplored. This paper evaluates two VLMs on extracting structured knowledge, comparing two prompting strategies: standard instruction-guided versus an augmented approach that cues troubleshooting layout patterns. Results reveal model-specific trade-offs between layout sensitivity and semantic robustness, informing practical deployment decisions.

