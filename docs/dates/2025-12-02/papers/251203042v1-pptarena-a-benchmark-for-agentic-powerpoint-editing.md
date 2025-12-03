---
layout: default
title: PPTArena: A Benchmark for Agentic PowerPoint Editing
---

# PPTArena: A Benchmark for Agentic PowerPoint Editing
**arXiv**：[2512.03042v1](https://arxiv.org/abs/2512.03042) · [PDF](https://arxiv.org/pdf/2512.03042.pdf)  
**作者**：Michael Ofengenden, Yunze Man, Ziqi Pang, Yu-Xiong Wang  

**一句话要点**：提出PPTArena基准和PPTPilot代理，以解决自然语言指令下PowerPoint可靠编辑的挑战。

**关键词**：PowerPoint编辑基准, 代理式编辑系统, 结构感知规划, 视觉语言模型评估, 文档级任务, 迭代验证

## 3 点简述
- 核心问题：现有方法在真实幻灯片编辑中缺乏可靠性和视觉保真度，尤其在长时程任务中。
- 方法要点：PPTPilot代理通过结构感知规划、程序化工具路由和迭代验证循环实现精确编辑控制。
- 实验或效果：PPTPilot在复合、布局敏感和跨幻灯片编辑上超越现有系统10个百分点以上，提升视觉一致性和保真度。

## 摘要（原文）

> We introduce PPTArena, a benchmark for PowerPoint editing that measures reliable modifications to real slides under natural-language instructions. In contrast to image-PDF renderings or text-to-slide generation, PPTArena focuses on in-place editing across 100 decks, 2125 slides, and over 800 targeted edits covering text, charts, tables, animations, and master-level styles. Each case includes a ground-truth deck, a fully specified target outcome, and a dual VLM-as-judge pipeline that separately scores instruction following and visual quality using both structural diffs and slide images. Building on this setting, we propose PPTPilot, a structure-aware slide-editing agent that plans semantic edit sequences, routes between high-level programmatic tools and deterministic XML operations for precise control, and verifies outputs through an iterative plan-edit-check loop against task-specific constraints. In our experiments, PPTPilot outperforms strong proprietary agents and frontier VLM systems by over 10 percentage points on compound, layout-sensitive, and cross-slide edits, with particularly large gains in visual fidelity and deck-wide consistency. Despite these improvements, existing agents still underperform on long-horizon, document-scale tasks in PPTArena, highlighting the remaining challenges in reliable PPT editing.

