---
layout: default
title: RFKG-CoT: Relation-Driven Adaptive Hop-count Selection and Few-Shot Path Guidance for Knowledge-Aware QA
---

# RFKG-CoT: Relation-Driven Adaptive Hop-count Selection and Few-Shot Path Guidance for Knowledge-Aware QA
**arXiv**：[2512.15219v1](https://arxiv.org/abs/2512.15219) · [PDF](https://arxiv.org/pdf/2512.15219.pdf)  
**作者**：Chao Zhang, Minghan Li, Tianrui Lv, Guodong Zhou  

**一句话要点**：提出RFKG-CoT，通过关系驱动自适应跳数选择和少样本路径指导，解决知识图谱问答中LLM幻觉问题。

**关键词**：知识图谱问答, 自适应跳数选择, 少样本学习, 上下文学习, 幻觉缓解, 推理路径指导

## 3 点简述
- 核心问题：LLM在知识密集型QA中因参数知识限制产生幻觉，现有方法如KG-CoT存在跳数选择僵化和路径利用不足。
- 方法要点：引入关系驱动自适应跳数选择器，动态调整推理步数；结合少样本上下文学习路径指导机制，增强LLM对推理路径的理解。
- 实验或效果：在四个KGQA基准测试中，RFKG-CoT相比KG-CoT提升准确率最高达14.7个百分点，消融实验证实组件互补性。

## 摘要（原文）

> Large language models (LLMs) often generate hallucinations in knowledge-intensive QA due to parametric knowledge limitations. While existing methods like KG-CoT improve reliability by integrating knowledge graph (KG) paths, they suffer from rigid hop-count selection (solely question-driven) and underutilization of reasoning paths (lack of guidance). To address this, we propose RFKG-CoT: First, it replaces the rigid hop-count selector with a relation-driven adaptive hop-count selector that dynamically adjusts reasoning steps by activating KG relations (e.g., 1-hop for direct "brother" relations, 2-hop for indirect "father-son" chains), formalized via a relation mask. Second, it introduces a few-shot in-context learning path guidance mechanism with CoT (think) that constructs examples in a "question-paths-answer" format to enhance LLMs' ability to understand reasoning paths. Experiments on four KGQA benchmarks show RFKG-CoT improves accuracy by up to 14.7 pp (Llama2-7B on WebQSP) over KG-CoT. Ablations confirm the hop-count selector and the path prompt are complementary, jointly transforming KG evidence into more faithful answers.

