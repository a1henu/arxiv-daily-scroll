---
layout: default
title: Even with AI, Bijection Discovery is Still Hard: The Opportunities and Challenges of OpenEvolve for Novel Bijection Construction
---

# Even with AI, Bijection Discovery is Still Hard: The Opportunities and Challenges of OpenEvolve for Novel Bijection Construction
**arXiv**：[2511.20987v1](https://arxiv.org/abs/2511.20987) · [PDF](https://arxiv.org/pdf/2511.20987.pdf)  
**作者**：Davis Brown, Jesse He, Helen Jenne, Henry Kvinge, Max Vargas  

**一句话要点**：探索OpenEvolve在组合双射发现中的应用与挑战

**关键词**：进化程序合成, 组合双射发现, 大语言模型, Dyck路径, AI辅助数学发现

## 3 点简述
- 核心问题：组合双射发现，特别是涉及Dyck路径的开放问题。
- 方法要点：使用OpenEvolve系统，结合LLM团队生成并演化候选代码。
- 实验或效果：应用于三个双射问题，发现系统有潜力但需人类辅助。

## 摘要（原文）

> Evolutionary program synthesis systems such as AlphaEvolve, OpenEvolve, and ShinkaEvolve offer a new approach to AI-assisted mathematical discovery. These systems utilize teams of large language models (LLMs) to generate candidate solutions to a problem as human readable code. These candidate solutions are then 'evolved' with the goal of improving them beyond what an LLM can produce in a single shot. While existing mathematical applications have mostly focused on problems of establishing bounds (e.g., sphere packing), the program synthesis approach is well suited to any problem where the solution takes the form of an explicit construction. With this in mind, in this paper we explore the use of OpenEvolve for combinatorial bijection discovery. We describe the results of applying OpenEvolve to three bijection construction problems involving Dyck paths, two of which are known and one of which is open. We find that while systems like OpenEvolve show promise as a valuable tool for combinatorialists, the problem of finding novel, research-level bijections remains a challenging task for current frontier systems, reinforcing the need for human mathematicians in the loop. We describe some lessons learned for others in the field interested in exploring the use of these systems.

