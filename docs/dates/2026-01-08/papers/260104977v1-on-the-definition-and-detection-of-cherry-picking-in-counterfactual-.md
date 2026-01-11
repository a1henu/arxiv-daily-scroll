---
layout: default
title: On the Definition and Detection of Cherry-Picking in Counterfactual Explanations
---

# On the Definition and Detection of Cherry-Picking in Counterfactual Explanations
**arXiv**：[2601.04977v1](https://arxiv.org/abs/2601.04977) · [PDF](https://arxiv.org/pdf/2601.04977.pdf)  
**作者**：James Hinns, Sofie Goethals, Stephan Van der Veeken, Theodoros Evgeniou, David Martens  

**一句话要点**：定义反事实解释中的选择性呈现问题，并研究其检测的局限性

**关键词**：反事实解释, 选择性呈现, 可解释人工智能, 检测局限性, 解释审计

## 3 点简述
- 核心问题：反事实解释存在多种有效方案，可能导致提供者选择性呈现以操控叙事
- 方法要点：基于可接受解释空间和效用函数，形式化定义选择性呈现，并分析不同访问权限下的检测能力
- 实验或效果：实证显示选择性呈现与基线解释在标准质量指标上统计不可区分，检测实践受限

## 摘要（原文）

> Counterfactual explanations are widely used to communicate how inputs must change for a model to alter its prediction. For a single instance, many valid counterfactuals can exist, which leaves open the possibility for an explanation provider to cherry-pick explanations that better suit a narrative of their choice, highlighting favourable behaviour and withholding examples that reveal problematic behaviour. We formally define cherry-picking for counterfactual explanations in terms of an admissible explanation space, specified by the generation procedure, and a utility function. We then study to what extent an external auditor can detect such manipulation. Considering three levels of access to the explanation process: full procedural access, partial procedural access, and explanation-only access, we show that detection is extremely limited in practice. Even with full procedural access, cherry-picked explanations can remain difficult to distinguish from non cherry-picked explanations, because the multiplicity of valid counterfactuals and flexibility in the explanation specification provide sufficient degrees of freedom to mask deliberate selection. Empirically, we demonstrate that this variability often exceeds the effect of cherry-picking on standard counterfactual quality metrics such as proximity, plausibility, and sparsity, making cherry-picked explanations statistically indistinguishable from baseline explanations. We argue that safeguards should therefore prioritise reproducibility, standardisation, and procedural constraints over post-hoc detection, and we provide recommendations for algorithm developers, explanation providers, and auditors.

