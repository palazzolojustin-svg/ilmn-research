

ILMN, TXG, and PACB: 3Q26 and 4Q26 Genomics Demand, Sequencing, and Spatial Trends With Sanofi's Head of Genomics 

Primary: ILMN TXG PACB Associated: ROP:SWX BRKR Stellaromics Inc. 



Viewpoint: Customer Moderator: Andrew Carmen (AC) | Oct 05, 2026 | 41 Min Read 

Seth Garren (SG), Senior Principal Scientist and Head of Genomics - Sanofi 

# **SUMMARY** 

# **Overview** 

The discussion examined sequencing, single-cell, long-read, and spatial-genomics adoption within preclinical biopharma research. Demand is rising as CRISPR validation, Perturb-seq, isoform profiling, and high-dimensional disease analysis become more routine. Purchasing decisions remain constrained by capital-budget cycles, data-security requirements, and the need to prove workflow compatibility. 

# **Key Insights** 

- Sequencing volume increased substantially as experiments expanded to millions of cells. Spending also rose, although larger flow cells lowered unit costs. 

- Single-cell analysis has replaced bulk RNA sequencing as the default for many projects. Growth is being driven particularly by CRISPR-based target validation. 

- AI-assisted coding is reducing analysis bottlenecks by accelerating computational work and enabling scientists to perform routine queries independently. 

- Long-read demand is emerging around neurological and rare-disease isoform profiling. Projects are currently outsourced while an internal platform purchase is evaluated. 

- Spatial genomics could support larger cohorts and broader discovery panels. However, chemistry comparability and real-world sensitivity must be validated before existing workflows are retired. 

- The expert expects industry demand for high-dimensional biological data to rise, but does not yet see broad proprietary data generation solely for AI training. 

The moderator repeatedly pursued the implications of platform economics, AI-enabled demand, and whether new spatial systems could replace established workflows. 

# **Competitive Landscape** 

Confidential 

11/04/2026 at 17:38 PM UTC 1 

|Company or platform|Positioning and outlook|
|---|---|
|Illumina NovaSeq X<br>Plus|Current high-throughput workhorse. Its installed base, workflow compatibility, and lower cost<br>than older instruments are major advantages. Market share may weaken if sequencing costs do<br>not remain competitive.|
|10x Genomics Flex v2|Dominant single-cell workflow and central to CRISPR validation. More than 90% of non-bulk<br>sequencing usage is associated with this platform.|
|PacBio|Favored internally for accurate long-read applications, with Vega supporting pilots and Revio<br>handling larger projects.|
|Oxford Nanopore|Remains a credible long-read alternative under evaluation, particularly where very long reads<br>offer value.|
|AXELIOS SBX|Viewed mainly as a high-capacity short-read competitor rather than a substitute for traditional<br>long-read systems. Attractive economics are offset by capital-cycle inertia.|
|Atera|Expected to supplement Xenium and potentially replace GeoMx or paired single-nucleus<br>validation. Two systems are preordered, with a possible third.|
|Pyxa|Three-dimensional capability is interesting, but current applications do not clearly justify<br>prioritizing depth over broader custom panels.|



# **Quantitative Insights** 

|Metric|Detail|
|---|---|
|Annual sequencing spend|Approximately 25% higher|
|Experiment scale|Roughly 1 million to 8 million cells|
|Main flow cell|25 billion reads; future needs may reach 25 billion to 50 billion|
|NovaSeq X Plus economics|About one-third of the cost of older NovaSeq 6000 workflows|
|Single-cell share|More than half of the expert’s activity and about half of spending|
|Instrument depreciation cycle|Approximately eight years|
|Legacy tissue inventory|Nearly 1,000 FFPE blocks|
|Budget pressure|Reagent funding was exhausted for the first time, primarily due to Perturb-seq growth|



AC: Hello, everyone. This is Andrew Carmen with Guidepoint. Thanks for joining us on our discussion of ILMN, TXG, 



Confidential 

11/04/2026 at 17:38 PM UTC 2 

and PACB: 3Q26 and 4Q26 Genomics Demand, Sequencing, and Spatial Trends With Sanofi's Head of Genomics, Dr. Seth Garren. Before we start, I just need to read some brief prepared statements. We kindly ask the advisor to refrain from any comment on stocks, stock prices, valuation, overall investment recommendations, material covered under an NDA, and material nonpublic information. 

If anyone has questions, please email ask@guidepoint.com. With that out of the way, very happy to have with us once again, Dr. Garren, who is currently the Senior Principal Scientist and Head of Genomics at Sanofi. I welcome you once again today. And if you'd like to just give us a brief background of yourself, we can get on to that and get right into the agenda. 

SG: Yes. Thank you. So yes, my responsibilities are within the research arm, so I'm predominantly involved in preclinical research. My team is responsible for high-dimensional data generation. Although in this past year, we've also taken on complex in vitro modeling. 

So we are also increasing the application of earlier complex modeling for eventually working through the NAMs initiative to reduce reliance on animal models and to get more complex target differentiation. But in general, we are early adopters of new sequencing technologies in single cell bulk and spatial space and have routinely advised on this topic for any stakeholders who are interested in tracking the trajectories of those markets. 

AC: It's been a while since we last spoke. What are you seeing directionally in regard to sequencing volumes and instrument consumables purchasing across biopharma and specifically to the NovaSeq X and related? 

SG: So I can speak to my own internal usage, which has been accelerating this past year due to the adoption of the 10x Genomics Flex v2, also known as Apex, and incorporating that into a Perturb-seq application. So as we've been increasing our CRISPR usage internally, the demand for more 1 million-8 million cell experiments has increased over years past, which has caused more large-scale experiments where we're buying more NovaSeq X 25B kits than we have previously. 

AC: Is that fundamentally year-over-year change that's significant in the number of kits and number of dollars spent? 

SG: Yes. I would say that on the raw sequencing side, we have a noticeable increase in spending on the kits, especially the size and volume of kits compared to the past. I think previously, we would spend - we would buy a larger number of smaller kits, and now we're buying a small number of larger kits. So I think from the nominal value, it might be slightly higher, but in terms of the volume of sequencing, it's definitely increasing. 

AC: Is that because they're getting cheaper per sample basically when you're going into larger kits? 

SG: Yes, there's that aspect. There's also the frequency at which we're running the sequencing protocols. I think we - ours are kind of colliding a lot at the end of the year, but we're definitely doing more higher volume sequencing. 

AC: And just from a year-over-year basis, as a total spend, is it up like 5%-10% or is that mischaracterizing? 

SG: I'd say it's probably - I'd put about 25% increase over last year. 

AC: Are you looking at getting new NovaSeq X replacements at this point? 

SG: We have two older NovaSeq 6000, which have gone off service, but we're still using them more for walk-up usage. The workhorse of our current usage is on a single NovaSeq X because we can run two 25B flow cells in tandem. So that's been sufficient for our current throughput rate. However, we did have another department, which is doing more secretome profiling needed to scale up and then ended up buying their own NovaSeq X because they're 



Confidential 

11/04/2026 at 17:38 PM UTC 

3 

running that constantly as well. So I think the sequencing demand for different activities was driven on our side by Perturb-seq and on their side by Olink. 

AC: So that was driving the volume. You mentioned 25B. Are you looking at the new news as well, the 35B? 

SG: So my understanding is that like they were kind of speaking in terms of like vague terms of what it can output, but we haven't specifically scaled up to like the higher one yet, though we might. And then as far as the newer sequencers, I think it's more of a capex commitment. But for now, we've been designing primarily around the 25Bs until we reallocate accordingly. 

AC: And they actually can deliver the 35B as well. But no, there's no like thoughts and plans to start investigating them as soon as available? 

SG: We try to keep on top of that as it is. But as new announcements come out, it's based on how often we're made aware of them and then incorporating that into our spending plans. 

AC: Yes. Just kind of looking at you have an interesting situation given that you still have some older instruments. So what's the big driver? Is it replacing old instruments with new instruments or getting more capacity or is there some sort of combination? 

SG: So we had to argue pretty heavily to get the NovaSeq X Plus in the first place because our capex governance was noticing that we still had two NovaSeq 6000s that were within the depreciation cycle. And as such, we'd argue that because with the newer sequencer, it made the higher volume sequencing less expensive than running it on the 6000s. 

So at this stage, the 6000s are now used more for ad hoc walk-up usage where you might have like a project that needs a little like less sequencing for maybe a single cell readout and to be available for that usage, but they're not kind of the workhorse anymore that they used to be. And that's because it's about 33% the price to run it on the X Plus than it is to run it on the old 6000s. So I think each new iteration does significantly drop the price of the sequencing, but that's balanced against the capex inertia from depreciation budgeting. 

AC: You mentioned you're running more 10x. You got the new Chromium Flex as well. Is that increasing - how much utilization increase is that? 

SG: So I think 10x is our workhorse, so nearly all of our non-bulk sequencing is via 10x at the current stage. So unless we're doing the occasional like bulk RNA-Seq experiment or whole genome experiment that I'd say over 90% of our usage is directly related to the Flex v2/Apex kit. 

AC: And just year-over-year, is that also up similarly to what you've seen for Illumina? 

SG: Are you saying is 10x up or is the- 

AC: Yes, 10x utilization. 

SG: Yes. Our 10x utilization has accelerated because we've started taking - because we've added the CRISPR projects on. So in the past, we would mostly do mechanistic experiments on like MOA projects or disease profiling. And now we've added on the CRISPR validation on top of it, so that's also increased our wide range of budget consumption because now the team that would normally do mostly cell culture reagent purchases are now doing cell culture plus 10x plus Illumina purchases. 

AC: Was there any long-read utilization in your facility? Are you looking at that? 



Confidential 

11/04/2026 at 17:38 PM UTC 4 

SG: So we're in the process of evaluating internalization of long-read. But right now, our current long-read projects are being outsourced, and that's due to a recent increase in interest in isoform profiling. So we've had, as of this year, multiple requests from both neurology projects as well as rare disease projects that have taken an interest in isoform profiling. 

And so we're working with multiple external solution providers to provide that in the short term. We do have a PacBio instrument in our CMC division that we can kind of use temporarily. But eventually, once those workflows get up and running, we will need to get an in-house long-read sequencer, and we're now making decisions between PacBio and ONT or any other alternatives. 

AC: Is the Revio somewhat favored? Or is that just to be determined? 

SG: So I think there's a lot of prejudice in favor of it. But as I've learned more, I think that it's been a bit of an apples and oranges comparison. So I need to educate myself further about what the actual trade-offs are between those long reads as this is the first time I've seriously considered making a pitch for one. 

AC: And is this for a 2027 purchase at this point? 

SG: Yes. So it would be - we would make the pitch in '27 to acquire one. And so what we would do is we're taking our outsourced projects and using that to run a pilot, which we can then develop a processing pipeline. And at that point, we'll have the basis to make a capex request. 

AC: And from what you're saying, while you do have the PacBio instrument in-house, you're outsourcing as well. And is that both on PacBio and ONT or something else? 

SG: We have some projects outsourced to PacBio, and outsourced to ONT. The one we have in-house isn't physically in the same build. It's in Sanofi, but it's not at the other location at a different site. So we're kind of - it's a bit ad hoc and piecemeal. So I think once we get the vision together, we will come with a more streamlined workflow that doesn't require so many moving pieces. 

AC: Regarding the other Sanofi instrument, I don't know if you mentioned, but was that the newer Revio or again or not? 

SG: They had gotten the newer Revio, but I think we were just running it on the Vega. So it depends on the scale of the project and also whether or not we were leveraging the Kinnex chemistry. 

AC: So the Vega is for kind of starting your pilot scales? 

SG: Yes. And then if we had a more aggressive one, we would move it to the Revio. 

AC: Do they just have one Vega as well as the Revio? 

SG: Yes, yes, that's correct. Yes, they've got one. 

AC: I think we talking kind of the sequencing, we'll have to get back with you regarding some of your thoughts and decisions regarding what you're going to do in long read. It sounds like that's still in process. But from the pharma perspective, I just wanted to get some idea if this AXELIOS SBX for long-read platform since we were talking about long read would have a meaningful impact on sequencing, and how would that relate to Illumina usage? 

SG: So I think like at first glance, you'd look at the numbers and you think, wow, these are a very compelling case for 



Confidential 

11/04/2026 at 17:38 PM UTC 5 

adoption. But I think the issue with industry is that there's a lot of inertia, especially with capex and depreciation budgets that would kind of necessitate that. So in a way, I would say the AXELIOS is not competing with the NovaSeq of today. 

They're really competing with whatever Illumina will have on the menu by the time the existing depreciation budgets would loosen up capex restrictions to consider a purchase. Because I think right now, it would be a very difficult order to argue for that merely on the basis of cheaper sequencing unless the volumes become prohibitive. 

AC: So if read length isn't as long as like the PacBio or ONT. So is it competing with them or is it not really not the case? 

SG: I tend to think of SBX more in terms of a short read alternative, like it's a long, short read rather than a short, long read. So I would consider it more competing in the space. It's compatible with 10x workflows. It's a cheaper per kit to hit the same number of reads. So it would - I would kind of frame it in those terms, whereas with the long read, usually the types of situations that would necessitate a long read benefit more from longer reads, in which case, I would say it's less likely to eat the lunch of the other two traditional platforms. 

AC: In regard to the ability to retain epigenetic mostly methylation information on PacBio and ONT, is that a big advantage for them compared to AXELIOS? 

SG: Potentially. I think it depends on how much that particular readout is leveraged. In my own experience, like that hasn't been high on the list of how we proceed with epigenomic profiling. But if that became a higher priority within our TA stakeholders, and that would certainly be a compelling argument. 

AC: Is there any use case for you for AXELIOS or perhaps not in the research end? 

SG: The only use case for it would be if the 10x or if our NovaSeq X reaches the end of its life cycle, and we're looking to replace it with something that's cheaper or if we're hitting very aggressive sequencing volumes. So for me, the best use case is the fact that you can get like 40 billion reads for like a tenth of the price, so that's really compelling to push it further. But right now, merely like while it is a compelling per kit cost difference, that's canceled out by the inertia of us having to deal with the depreciation over about an eight-year period with our internal finance cycle. 

AC: So that's a long time for a sequencing platform. 

SG: Correct, which means that we're always going to be in the case where at any given moment in the market, there's going to be some new offering that is - has superior metrics to what we're using, but the superior metrics on their own are not sufficient to justify ripping out everything and immediately adapting to it. 

AC: And then regarding the space that you're working in, do you see multiple sequencing platforms coexisting well within your facility? 

SG: The ones that would coexist the best would be like an Illumina and a ONT or an Illumina and a PacBio would make the most complementary sense. But if you start stacking like Illumina and SBX or PacBio and ONT, it starts to get a little redundant. 

AC: Do you have any interest in these new platforms, and this is kind of relating more to spatial, the Pyxa? 

SG: So we've been poking around some of the 3D spatial. I think doing deep in CT spatial is interesting. But I think we've been struggling with how to create an actionable utilization of the deeper three dimensions outside of very focused questions like endothelial proximity or highly structured biology. 



Confidential 

11/04/2026 at 17:38 PM UTC 

6 

So I think most of our spatial applications were interested in things like immuno-oncology, tumor infiltration, autoimmunity with like tertiary lymphoid structures and kind of coming up with kind of broad strokes geography of where and when are certain targets of interest observed for disease profiling. And so while something like the Pyxa could give you that extra like 100-micron depth, it's still a bit constrained on the target volume. 

So we'd have to kind of reorient our thinking around like, ok, what decisions are we struggling to make for want of the Z-axis that while we're currently exploring the decisions we're struggling to make for want of a larger custom panel. And so along those lines, we're a bit anchored to the Atera as our next spatial investment that we've already preordered and how that can impact both our existing Xenium workflows as well as potentially our NanoString workflows for the GeoMx specifically. 

AC: I probably should put that question here closer to the Atera. Ok. Actually, let's get back to that then. Before we move on from this question too, I wanted to know, you talked about the different platforms and potential. What's the most important thing for you? Is it the cost, turnaround time for sequencing? What is it that makes you decide for one platform versus another at this point? 

SG: Well, it depends on what flavor. If we're talking about like an SBX versus an Illumina, I think like basically, the cost and sequencing volume would be the top one. So because we're pushing more and more cells, we're going to need more and more reads. So you could get a cheap sequencer, but it caps out at 10 billion, that's not going to work. 

So if it can get at least 25 billion-50 billion, and then when you get - that gets into the ballpark and then we see how much of a price differential there is. So because the SBX could get you 40 billion for like significantly less than a 25B kit would cost, that would be the argument to do it. 

And when we made our NovaSeq X argument, it was on the same basis, it was comparing the cost of sequencing, like how much would it cost to sequence 25 billion reads on two NovaSeq 6000s compared to one NovaSeq X Plus. 

And then when we presented that, it was basically one-third of the price. So that's how we justified it by saying that we anticipate an explosion in sequencing volume due to increasing numbers of single cells. And as such, we're going to need more powerful and cheaper sequencing and that same argument would apply at later generations. 

AC: Do you see Illumina still having the ability to maintain their cost competitiveness compared to these new platforms? 

SG: That remains to be seen, but I think Illumina seems to be kind of branching in a variety of directions like trying to take on single cell and spatial offerings to just be more of a Swiss Army knife rather than a specialist. That can be a dangerous strategy when you're getting outcompeted on each individual axis and you become kind of a jack of all trades, master of none. 

But they do have - they get a head start from the installed basis and the inertia from the cost of transition, but that can't hold them indefinitely. And if they don't have an answer to significantly cheaper sequencing at the same depth, then they will start to lose market share. 

AC: You don't think that their ability to fully support and incorporate entire workflows would have an advantage to them? 

SG: In a world without strict digital security, that would be a great strategy, but I've struggled to leverage any of their workflow support because it basically, like I have to somehow get institutional support from our digital division to like give us all the data security permissions to send the data out and use cloud solutions and all that. So it's unfortunately, just not realistic within any of the companies I've worked at to easily leverage vendor for end-to-end workflows unless 



Confidential 

11/04/2026 at 17:38 PM UTC 7 

it's like physically in the instrument. 

AC: Is that more true for biopharma versus like university? 

SG: A university, I can't imagine, has anywhere near the same like guardrails that biopharma does. So I think a university would be a much better fit for these end-to-end solutions. Maybe if like a core facility or a department can leverage that and just have grants to pay for it, that's all fine and good. 

But every time I've attempted to use these, I just - basically I am told no by digital, like and that it would take massive lobbying that convince digital's leadership to prioritize this when you now also have every other vendor of every other modality of every other activity research could be doing also asking digital for the same thing. And then they're trying to maintain data security on that. So it's a more fundamental problem than merely whether or not the vendor can offer the capability. 

AC: How do you deal with that friction regarding that and how it would limit your ability to take on this new technology? 

SG: I keep it internal. So I take on the new technology, it generates the same types of files and then I just process them through the same pathways internally. So yes, while the vendor offers a nice solution, so I don't have to keep building these internal pipelines, unfortunately, the solutions are just simply disallowed, so. 

AC: So you have to internalize and build your pipeline and have your internal support. 

SG: Yes. And then the good news is that a lot of the vendors will keep things compatible. So it's not like - so like an SPX is compatible with the 10x library prep and its output files that are compatible with barcode matrix generation. And so you can slot it in more or less, but if Illumina says, well, we can offer all those things as a convenience, like, well, that's nice, but I can't use it. I'm not allowed to. So that's not a point of competition for a customer like me. 

AC: Has single cell moved further toward routine biopharma use since previous conversation? It sounds like with CRISPR potentially, but - and are increasing experiment volumes and reagent utilization being observed rather than just broader interest in the technology? 

SG: Yes, like it's gone from bulk RNA-Seq to be my bread and butter to single cell Flex being the bread and butter. So that's kind of our new default project. We kind of start with that, and then we'll only come up with bespoke reasons to argue for something outside of that accordingly. So the culture is somewhat shifted to single cell until a reason to do something else. 

AC: Does single cell make up a large part of your business at this point? 

SG: Yes. Like my own activities are, I'd say, over half is single cell. Like we have spatial, we've got complex modeling. We've got bulk whole genome, but then we've got like especially in terms of spending, it's pretty much half of it is pure single cell, either single cell preclinical project support or single cell target validation. 

AC: Regarding the single cell, it sounds like it's getting more embedded in standard drug discovery. Do you see it as continuing to grow in utilization from what you're seeing? 

SG: Yes. I think the big potential for growth is if translation and development start taking it up more or if they open up more reverse translation. I think there's no shortage of appetite for single-cell data. We're trying to collect and centralize it, and there's a lot of external Atlas initiatives that people are interested in collecting from. 



Confidential 

11/04/2026 at 17:38 PM UTC 

8 

So I think like a lot of the bulk RNA data has largely been harvested for the obvious target, and now we're kind of moving toward more higher dimensional alternatives with more nuance to them like single cell. 

AC: You mentioned, I believe this was looking back at our last transcript, that the data analysis was somewhat bottleneck for single cell. Has that improved since that time? 

SG: So I think one of the biggest differences in the past year is the increased adoption of Claude vibe coding. So at least in my own observation that we've been using it to, one, accelerate computational biologist activities so that they don't have to spend time doing the boring stuff of just formatting the images and the data wrangling. 

And two, empowering end users to query the data, so we don't have as many of those email bounce exchanges where a bio lead asks the comp bio like, hey, can you look up this gene or hey, can you zoom in on this cell resolution and they can just do it themselves by using Claude. Whether that's sustainable is a separate question with the trajectory of the cost of AI usage, but that is an observation anecdote that I can provide that's different from last year. 

AC: And that's significant and the ability to drive that increase that you were speaking of? 

SG: Increase in demand or increase- 

AC: Increase in both - well, if you can't analyze, you can't run more, I would assume. But getting through those bottlenecks allows you to run more experiments, essentially? 

SG: Well, no. So the reason I ask that is because you can have projects where you just have a bigger project with fewer analysts or you have a higher number of projects with more democratized analysis. 

So in our case, like I guess it is both, like we do have bigger projects with more analysis, but we also have more cases of people taking their projects end-to-end by leveraging these more user-friendly options for kind of doing the basics. So like I can comment that my own team members are getting deeper into the analytical workflow because they're able to ask Claude to like run a routine Seurat type analysis for them. 

AC: So you're seeing expanding opportunities because of Claude? 

SG: Yes. Yes, in both directions. And that's been incorporated into our department communications, so that we have the user end and we have the comp bio end. So accelerate comp bio and democratize the user. 

AC: So that's a significant change. What should we expect for next year? Is it continuing in the same trajectory? 

SG: Assuming the token prices don't skyrocket, we'll probably try going in that direction. For next year, we're going into combinatoric validations. So now we're going to start putting multiple targets in the same cell, and that will also have a fairly aggressive requirement. And then we're also - yes, so I think as far as the things that I know are on the calendar, they're kind of expansions of a lot of this year's pilots turn into larger scale projects. 

AC: You mentioned the CRISPR is driving some things. Are there other multi-omic capabilities that are driving additional usage? 

SG: Let's see. So we have CRISPR. I know we're interested in like surfaceome, but I think we're - we haven't decided which modality we're going to use for that. And then, of course, like we've also had some interest in DNA profiling. And I keep flirting with like Mission Bio and like maybe we should consider or maybe not. But in this case, if we're looking at certain types of cell line profiling that may be a niche application, but maybe we'll just outsource it. 

So I'm not saying that we would invest in it, but that's a little bit outside the normal scope. But as far as things like 



Confidential 

11/04/2026 at 17:38 PM UTC 9 

ATAC or methylation or some of these other modalities, we haven't quite gotten to the point where those have become major decision drivers yet. 

But that can always change because the nature of storytelling in pharma kind of depends on communal comfort with the dimension of biology that's being looked at. And the fact that I'm seeing isoforms suddenly become relevant now is interesting because in the past, splicing was just something people ignored. 

AC: So is that the bigger growth area for you in single cell? 

SG: Yes. We're doing bulk splicing now. We've entertained single-cell isoform for that, but we ended up exiting that because it just didn't amount. So like we have an ICELL8, which was able to do the well-based full-length single cell, and we ended up just discontinuing it because we just couldn't find the use case for it. 

But that was also more in a like a gene counting context. But if we're doing things like hunting for new fusion proteins or new like tumor-dependent isoforms or other exotic biology then - that it might come back. But it's not as front and center as like Perturb-seq or Iso-Seq. 

AC: You had mentioned you're testing and potentially getting Atera soon. What's your opinion about the instrument, and how are you going to use it? 

SG: So with the Atera, it basically starts to open up the potential of the Xenium, at least on paper. We'll have to see how it executes. But one of the big problems with spatial is sample volume. So like I think traditionally, we could get like maybe around two, maybe three samples on a Xenium slide, and then we have two Xenium instruments, so we can kind of run them aggressively and get like a modest number of samples. 

But with Atera, we can get larger slides and you can kind of have more aggressive TMA designs. And then with the kind of full transcriptome background, that lets us do a little bit of discovery and kind of tripping over some unexpected genes. So there's a chance it may replace our GeoMx, which is the current unbiased method for spatial. So we'll keep an eye on that. 

And then, of course, having the 1,000 Flex custom on top of it, which is how we've been trying to design most of our Xenium panels that way. So I think in the short term, we'll probably use it as a supplement to the Xenium. So you get like basically a third larger slide that could fit more things, and we have a similar panel across them and genes accordingly and try to see if the sensitivity differences throw off the comparisons. 

But more importantly, we're curious to see whether or not the unbiased like kind of wide dragnet transcriptome panels that Xenium has could replace our paired single cell that we usually do off the same block. 

AC: And how used is your current Xenium? I guess you have two Xeniums. Are they at high utilization rate at this point? 

SG: We use them mostly for disease profiling. So we will go shopping around for tissue samples from vendors. And then we will kind of generate as many samples as reasonable within a labor limit. And then we use that as part of our target credentialing requests where they might want to see a few more examples in the wild of how a target of interest looks within a certain disease indication. And then we've also leveraged like some services of 10x to have them run Xenium with both RNA and protein to help answer like a variety of programs about the same disease indication. 

AC: You mentioned that Atera is not initially going to replace that Xenium work, it's kind of an additional? 

SG: The Atera will supplement the Xenium and potentially replace the GeoMx. 



Confidential 

11/04/2026 at 17:38 PM UTC 

10 

AC: Ok. Got it. So that- 

SG: Or replace the paired single-nuc, sample single-nuc. 

AC: What do the economics of the Atera with the larger slides and things, does that give you the ability to run larger cohorts or multiple samples on the slide that going to make it beneficial at least from the cost of the actual experiments? 

SG: Yes. One of the big benefits is that you can have larger TMAs and start to get like numbers. So you can go from like spatial projects that have like four samples to more than that. So that's the hope, and we'll see how well that compares. I think the biggest uncertainty is whether there's going to be a major chemistry differential if we were to run a Xenium and an Atera in tandem with the subtle differences in the chemistry between the make it, so you can't compare the samples across them. 

AC: Do you think that's a to be determined, we'll have to ask you next year? 

SG: Yes. We're still - we can still look into that. But I think like if we're just counting genes, it should be ok. It depends on how rigorous your comparison background noise is, but we'll have to wait and see on that. If they are comparable, that creates an unfortunate situation, but I think it depends on the question you asked. 

AC: Do you think that if you have some whole transcriptome capability on that instrument that, that's going to be a benefit and potentially some differential versus a targeted spatial approach? 

SG: Yes. I recall that CosMx was experimenting with layering. They had their 18,000 and then you could throw - and I saw some users would throw 1,000 on top to kind of make their relevant biology of interest louder. 

I think it's a similar principle, but it remains to be seen, like is this just ones and zeros across everything and then you're just kind of getting an echo of a hint and then you still have to follow up with the bias panel? Or could it legitimately replace like the single-cell Flex validation that we've been running? 

AC: You've been running a lot of single cell over the years now that you have this new instrument coming on board, etc., that claims to have single-cell resolution. Do you foresee that any of your single-cell experiments would be shifting to the system or is it just not the case? 

SG: It depends on the - it depends on the nature of the cells being profiled. So obviously, to do spatial, it needs to be embedded and sectioned and not every biology benefits from that or warrants it. So I think like - I don't know that we're doing like a ton of the full tissue dissociation. So usually, if we're doing like a full tissue profiling, we'd go to spatial in the first place and then any additional dissociation would come from the single-cell Flex. 

I would say Atera could potentially replace the Flex validation and just validate itself using the whole transcriptome. But I think a lot of other ones we are doing like in vitro experiments, like we wouldn't necessarily like embed it and then run it on Atera in lieu of single cell because that's adding extra steps with more complication. 

So it really depends on what you're originally doing. Like if we were originally doing a lot of, say, mouse in vivo like tumor studies, and we were just dissociating the tumors left and right and not doing spatial, that would be one thing. But our usual default for a mouse tumor study would be a GeoMx run. So we take the tumor, embed it, run a section on GeoMx for spatial, and then run some more sections for single cell. 

AC: And would you just be buying - or if you have made that decision, would you just be buying the Atera? Is that sufficient for your needs for the future? 



Confidential 

11/04/2026 at 17:38 PM UTC 

11 

SG: Yes. We are buying an Atera then another department is also buying an Atera. And then we may get one for our European side that remains to be seen. 

AC: You mean like up to three Ateras as well. 

SG: Well, I can say two are definitely preordered and there might be a third. 

AC: When do you think you're going to get that so we can speak with you after? 

SG: So probably Q1 next year, we'll start installing and running it, and then we'll see how it goes. 

AC: So it sounds like it'd be interesting to see if it can actually deliver what they say it can. 

SG: Yes, I'm interested. But that's why I'm not like discontinuing things in anticipation. So we have the GeoMx and the Flex FFPE as back up. And then if it compares, then we could start transitioning away from either of those for our routine experiment design. 

AC: The instrument - I should say, they were talking about some automation on board for Atera. Does the initial instrument deliver with a high level of automation or is that something that's expanding with time? 

SG: Yes, I'm not entirely sure which segments we would take advantage of there. We currently use things like the BOND RX for upstream automation of like GeoMx experiments. But we haven't made decisions yet about like which of the specific sub offerings we would leverage just yet. We're trying to get it there and get our heads around how to use it and what it means. 

AC: And then just kind of the big questions here across sequencing, single cell, spatial, which you're doing all of them. Where is the greatest change that you're seeing in biopharma purchasing priorities and what technology improvements might drive material higher genomics volumes over the next year or two? 

SG: Well, across pharma, the biggest change is the demand for - is data demand. So everybody has these big data lakes and centralized AI training. And there's like - there's a bit of a debate going on about whether or not this is utterly quixotic or whether we're just on the cusp of coming up with a perfect virtual cell model. 

And so everyone is just kind of holding their breath and watching Genentech, like, attempt it. And my personal opinion is that we have to be more granular about that. But in general, like across pharma, I'm seeing just like endless demand for this kind of data. So someone somewhere is developing it, so I assume from a vendor standpoint, like they would be affected. 

So Illumina, 10x, and Roche, everybody would foreseeably see that if everybody, in fact, wants to train all these AI models on cell data, then the data must be generated somewhere. So I would imagine that, that would put an upward pressure on just global high-dimensional data generation across the entire market. But whether any given company does it is a more nuanced question. 

I can say that our company has kind of taken a more moderated approach where we'll get data from consortia that makes sense, but we're not going to like spin up some massive, like, cell virtual cell effort where we're going to just generate all the data ourselves, like we kind of do internal data generation for proprietary reasons, not just for bulk reasons. And then the rest, we just go shopping for external providers or groups like Tempus or Open Targets consortia or any other location you can find. 

AC: To get more data for your analysis, with regard to your internal process as well, do you have banks of samples that 



Confidential 

11/04/2026 at 17:38 PM UTC 12 

you could potentially utilize for these genomic assays? Or is that not a major driver at this point? 

SG: We do have biobanks. We also have like these legacy banks that we just finished cataloging. So there's like probably close to 1,000 FFPE blocks across like every indication that we've ever cared about ever. Obviously, a lot of those we've moved away from, but we have them. We're constantly shopping for new samples. We're also in very kind of invested negotiations with KOLs at various cancer centers to try to get access to certain precious patient samples for profiling. 

And in that case, we're either negotiating a difference between either having them give us a sample and then they just give us in the form of data or they give us access to the sample and then we profile it ourselves. But either way, we're trying to get high-dimensional data from these like nonresponder patient samples with certain leading approved drugs to kind of create a new context for what the new brave new world is in cancer treatment. 

AC: Just how important is this genomic analysis at this point for drug discovery and development? And where do you see it as being most important? 

SG: It's really important across the board. So I start with reverse translation. You asked what was different between the different subcategories, endotypes and responder and nonresponder signatures that can point to a mechanistic story of ways that, say, a tumor could escape or ways that the drug might fail, and that can give you insights as to the deeper biology. Then we can do disease versus healthy and come up with lists of potential candidates in general. 

Then we can do combinatorics, so we can ask which combinations of treatments might have very synergistic effects that the whole is better than sum of its parts. And then you come up with rankings. So we rank it all and say, ok, based on these proposals and these criteria and then things like on-target off-tumor effects or side effects or safety or efficacy evidence, we come up with those rankings, then we do validation, and we're back to the Perturb-seq discussion and saying within an in vitro context, is this behaving in the direction we would expect? 

Are there any surprises? Then we get into our kind of early-stage drug programs where we're creating candidates and profiling them that gets us into the mechanism of action where we're then using it to compare candidate A versus candidate B and C. 

Are they doing what we think they're doing and what makes them different from each other and how do we rank the candidates? Then you get into biomarker generation to say, ok, what's a good indication of whether the candidate would be likely to succeed or fail and what are the indications the candidate is, in fact, doing anything and providing that as translational research. 

And then there's also patient stratification of sequencing the diseases and biomarkers available to see if they can make any predictions about whether a patient is likely to be a good responder to a given candidate. So pretty much the entire workflow has some point where high-dimensional data generation comes into play. 

AC: You mentioned earlier regarding the AI helping to better expand your customer base or who's actually running. But do you see additional AI-driven demand for biological data sets that's materially going to increase sequencing or spatial volumes in this coming year beyond what we're already seeing? 

SG: It's tricky because - we have large data lakes. We have a centralized AI division. We've been mostly, this past year, just collecting all the data we already have and getting into the data lakes and getting it sorted and getting it ready for ingestion. 

We have not yet gotten to the point where they started pulling on us where they're like, ok, now we want you to start generating proprietary data to fuel these data lakes because I think it's still been just working through all the historic 



Confidential 

11/04/2026 at 17:38 PM UTC 

13 

data that we already have and all the external data that we're in the process of ingesting that I have not personally felt them come to me and say, ok, now I want you to actually start generating all the proprietary data that we would power a prediction algorithm for. 

But that doesn't mean it couldn't be around the corner. And that's just one potential, like future anticipation. It's just - they may come to me or they may go to Open Targets or they may go to a KOL or like - so the devil is in the details, but for me, yes, like the AI demand there will depend also on how well they clarify what questions it would answer because we're not doing the whole like we're just going to throw everything in there and hope it spits out like a perfect crystal ball of what cells do. 

And instead, we'd have to have these very specific questions we're trying to answer with a reasonable space of dimensionality to participate in where you could realistically get enough data to start to make a good prediction about it. And I haven't seen it coalesce around that yet. 

AC: Today, and you've said in the past too, it seems like you're pretty open to using the CROs, but you're also building internal capability and potentially you're also doing collaborations with academics and others. Where is that leaning? Are you building - is it leaning toward more internal capability at this point or is it more outsourcing? 

SG: I don't know that it like pushes one direction or another because each one has its own justification. So like if we go to a KOL, we may have them generate it because their own governance doesn't want them to be treated like a glorified biobank. So then we would just have them do the generation. 

But we might be able to negotiate a little bit of our own generation off of that, so we get some there. If we're outsourcing something, it's usually because we either lack the bandwidth or we lack the specific instrumentation. So in our case, we're doing more outsourcing to long read unless and until we buy our own long read and get it internalized. 

Whereas most of our internalization has been on validation workflows because we have all the pieces and it's already proprietary as it is. So we're not kind of doing a lot of bread-and-butter outsourcing. We're really only relying on external sources where there's a piece missing that could be filled in with the external solution. 

AC: Just relative to everything you're doing here, does that directive for onshoring, reshoring have any impact on you? And do you see any inflationary pressures as of late? 

SG: Everything is getting more expensive, but - and I would say that this is the first year we've run out of reagent budget. That's never happened before. So - but I think when we looked at that, that was because we were doing all the Perturb-seq, as I mentioned. 

And as far as offshoring, there is a very aggressive push among every pharma I've seen to do large molecule biologic screening in China. That's very popular right now. So China has pushed for these workflows where they just started printing every antibody anyone could think of and have these massive biologic libraries. And now everybody wants to just start screening those libraries with their favorite target and indication of interest. 

So we can start thinking of large molecules more like small molecules rather than doing all this homework before you attempt to inject an immune response. So that like we have our own footprint over there. Every company I know either has a collaborator or a footprint or a KOL or something in China that gives them a place there. So I think that's not going anywhere. 

AC: That's primarily R&D? SG: Yes. So it's- 



Confidential 

11/04/2026 at 17:38 PM UTC 

14 

But I guess you asked about like onshoring and stuff. Generally speaking, I'm not making decisions on that basis. Though I will say like if we find a solution provider because my cluster is split across two continents, we always ask solution providers if they have a presence in Europe so that my European counterparts have an easier way to get samples to and from them. 

So we usually try to keep Europe in Europe and North America in North America, but we're not necessarily like being told to prioritize our activities to like keep it onshore because of tariffs or something. Usually, we're just kind of finagling around like capex, like we had one case where we're trying to pitch to get a microscope - and like part of the capex had like a big tariff bill on it, but we found out that the software was not subject to the tariff. 

So we were like, ok, could you just take the software off the bill and we just download it and then paper it differently and that takes the tariff bill off of it or it reduces the tariff amount. So like that's the only thing that I could think of where we're actually incorporating that in our decision-making, and that was a bit more of like kind of accounting agility on the part of one of my team members. But for the most part, it's usually just what piece is missing and who can fill it in. 

AC: Would you like to make a concluding statement then to wrap us up for today? 

SG: Yes. So I think my concluding statement is always when you're looking for the implications on markets, especially vendors providing anything for high-dimensional data generation. I think the two markets I always keep an eye on every quarter is the clinical market to see if they've made any headway in increasing clinical adoption and not just diagnostics, but literally like doing reverse translation or even forward translation within the clinic because I think that's really the holy grail of like 10x Genomics. 

And then as far as like Illumina versus AXELIOS or any of these other newer technologies, the big thing is to keep in mind is the inertia of adoption of any given area. So I think academia seems more agile, but they're less funded, whereas the larger pharma industry is more funded but less agile. So it's not NovaSeq X versus AXELIOS. It's the - whatever Illumina comes up with after NovaSeq X that would be competing with AXELIOS because that's what I would be available to then ask the question of what I would get next. 

AC: I really appreciate you taking the time today. It's been a pleasure to speak with you once again. Thank you. 

DISCLAIMER: The statements or opinions expressed today are those of the Advisor and not Guidepoint, who disclaims all liability for the content provided. The Advisor may not disclose material nonpublic or confidential information or any information that would cause the Advisor to breach any duty or obligations. Guidepoint is not a registered investment advisor and the information provided is not intended to constitute investment advice. 



Confidential 

11/04/2026 at 17:38 PM UTC 15 

