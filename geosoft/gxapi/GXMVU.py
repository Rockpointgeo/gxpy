### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMVU:
    """
    GXMVU class.

    A catchall library for methods using the `GXMAP <geosoft.gxapi.GXMAP>` and `GXMVIEW <geosoft.gxapi.GXMVIEW>` classes.
    These include drawing flight paths, legends, postings, and
    special objects such as histograms and bar charts.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMVU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMVU`
        
        :returns: A null `GXMVU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXMVU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXMVU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def arrow(cls, mview, hx, hy, tx, ty, ratio, angle, type):
        """
        Draw an arrow.
        """
        gxapi_cy.WrapMVU.arrow(GXContext._get_tls_geo(), mview._wrapper, hx, hy, tx, ty, ratio, angle, type)
        



    @classmethod
    def arrow_vector_vv(cls, mview, vv_x, vv_y, vv_dx, vv_dy, scale, pos, size, style, point, thickness):
        """
        Draw arrow vectors based on input VVs.

        **Note:**

        The locations are given in two VVs, and the directions
        in the two others. A wide range of sizes are available.
        If the scaling is set to `rDUMMY <geosoft.gxapi.rDUMMY>`, then arrows are automatically
        scaled so the largest is 1cm in length.
        If the line thickness is set to `rDUMMY <geosoft.gxapi.rDUMMY>`, the line thickness scales
        with the arrow size, and is 1/20 of the vector length.
        """
        gxapi_cy.WrapMVU.arrow_vector_vv(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, vv_dx._wrapper, vv_dy._wrapper, scale, pos, size, style, point, thickness)
        



    @classmethod
    def bar_chart(cls, mview, group_name, data, line, x_chan, list, x_title, x_txt_size, y_title, y_txt_size, bar_title, bar_txt_size, bar_width, dist_fid, label, tick, right_axis, top_axis, bottom_axis, surround, left, bottom, right, top, xm, ym, widthm, heightm):
        """
        Plot bar chart on a map.
        """
        gxapi_cy.WrapMVU.bar_chart(GXContext._get_tls_geo(), mview._wrapper, group_name.encode(), data._wrapper, line, x_chan.encode(), list.encode(), x_title.encode(), x_txt_size, y_title.encode(), y_txt_size, bar_title.encode(), bar_txt_size, bar_width, dist_fid, label, tick, right_axis, top_axis, bottom_axis, surround, left, bottom, right, top, xm, ym, widthm, heightm)
        



    @classmethod
    def cdi_pixel_plot(cls, mview, group, data_va, elev_va, xvv, itr):
        """
        Create a color pixel-style plot of CDI data.

        **Note:**

        Draws a single colored rectangle for each data point in
        Conductivity-Depth data (for example). It is similar to the
        result you get if you plot a grid with Pixel=1, but in this
        data the row and column widths are not necessarily constant,
        and the data can move up and down with topography. The pixels
        are sized so that the boundaries are half-way between adjacent
        data, both vertically and horizontally.
        """
        gxapi_cy.WrapMVU.cdi_pixel_plot(GXContext._get_tls_geo(), mview._wrapper, group.encode(), data_va._wrapper, elev_va._wrapper, xvv._wrapper, itr._wrapper)
        



    @classmethod
    def cdi_pixel_plot_3d(cls, mview, group, data_va, elev_va, xvv, yvv, itr):
        """
        Create a color pixel-style plot of CDI data in a 3D view.

        **Note:**

        Similar to `cdi_pixel_plot <geosoft.gxapi.GXMVU.cdi_pixel_plot>`, but plotted onto a series of
        plotting planes which hang from the XY path in 3D. Each vertical plane azimuth
        is defined by two adjacent points on the path. The color "pixel" for each
        data point is plotted in two halves, with each half on adjacent plotting planes,
        with the bend at the data point.
        """
        gxapi_cy.WrapMVU.cdi_pixel_plot_3d(GXContext._get_tls_geo(), mview._wrapper, group.encode(), data_va._wrapper, elev_va._wrapper, xvv._wrapper, yvv._wrapper, itr._wrapper)
        



    @classmethod
    def color_bar(cls, mview, itr, decimal, ann, height, width, x, y):
        """
        Create a Color Bar in view
        """
        gxapi_cy.WrapMVU.color_bar(GXContext._get_tls_geo(), mview._wrapper, itr._wrapper, decimal, ann, height, width, x, y)
        



    @classmethod
    def color_bar2(cls, mview, itr, itr2, decimal, ann, height, width, x, y):
        """
        Create a Color Bar from two `GXITR <geosoft.gxapi.GXITR>`

        **Note:**

        The secondary `GXITR <geosoft.gxapi.GXITR>` is used to blend horizontally with the
        primary `GXITR <geosoft.gxapi.GXITR>` in each box.
        """
        gxapi_cy.WrapMVU.color_bar2(GXContext._get_tls_geo(), mview._wrapper, itr._wrapper, itr2._wrapper, decimal, ann, height, width, x, y)
        



    @classmethod
    def color_bar2_style(cls, mview, itr, itr2, decimal, ann, height, width, x, y, style):
        """
        Create a Color Bar from two ITRs with style options

        **Note:**

        The secondary `GXITR <geosoft.gxapi.GXITR>` is used to blend horizontally with the
        primary `GXITR <geosoft.gxapi.GXITR>` in each box.
        """
        gxapi_cy.WrapMVU.color_bar2_style(GXContext._get_tls_geo(), mview._wrapper, itr._wrapper, itr2._wrapper, decimal, ann, height, width, x, y, style)
        



    @classmethod
    def color_bar_hor(cls, mview, itr, decimal, ann, width, height, x, y, label_orient):
        """
        Create a horizontal color bar in view

        **Note:**

        The sign of the annotation offset determines whether labels are
        plotted above or below the colorbar. Labels above are text-justified
        to the bottom of the text, and labels below are text-justified to
        the top of the text.

        .. seealso::

            `color_bar <geosoft.gxapi.GXMVU.color_bar>`
        """
        gxapi_cy.WrapMVU.color_bar_hor(GXContext._get_tls_geo(), mview._wrapper, itr._wrapper, decimal, ann, width, height, x, y, label_orient)
        



    @classmethod
    def color_bar_hor2(cls, mview, itr, itr2, decimal, ann, height, width, x, y, label_orient):
        """
        Create a Horizontal Color Bar from two ITRs

        **Note:**

        The secondary `GXITR <geosoft.gxapi.GXITR>` is used to blend horizontally with the
        primary `GXITR <geosoft.gxapi.GXITR>` in each box.
        """
        gxapi_cy.WrapMVU.color_bar_hor2(GXContext._get_tls_geo(), mview._wrapper, itr._wrapper, itr2._wrapper, decimal, ann, height, width, x, y, label_orient)
        



    @classmethod
    def color_bar_hor2_style(cls, mview, itr, itr2, decimal, ann, height, width, x, y, style, label_orient):
        """
        Create a Horizontal Color Bar from two ITRs with style options

        **Note:**

        The secondary `GXITR <geosoft.gxapi.GXITR>` is used to blend horizontally with the
        primary `GXITR <geosoft.gxapi.GXITR>` in each box.
        """
        gxapi_cy.WrapMVU.color_bar_hor2_style(GXContext._get_tls_geo(), mview._wrapper, itr._wrapper, itr2._wrapper, decimal, ann, height, width, x, y, style, label_orient)
        



    @classmethod
    def color_bar_hor_style(cls, mview, itr, decimal, ann, height, width, x, y, style, label_orient):
        """
        Create a Horizontal Color Bar in view with style options
        """
        gxapi_cy.WrapMVU.color_bar_hor_style(GXContext._get_tls_geo(), mview._wrapper, itr._wrapper, decimal, ann, height, width, x, y, style, label_orient)
        



    @classmethod
    def color_bar_style(cls, mview, itr, decimal, ann, height, width, x, y, style):
        """
        Create a Color Bar in view with style options
        """
        gxapi_cy.WrapMVU.color_bar_style(GXContext._get_tls_geo(), mview._wrapper, itr._wrapper, decimal, ann, height, width, x, y, style)
        



    @classmethod
    def color_bar_reg(cls, mview, itr, itr2, reg):
        """
        Create a Color Bar in view

        **Note:**

        To allow for expansion, all parameters are passed inside the `GXREG <geosoft.gxapi.GXREG>` object.
        
        BAR_ORIENTATION        one of MVU_ORIENTATION_XXX (DEFAULT = `MVU_ORIENTATION_VERTICAL <geosoft.gxapi.MVU_ORIENTATION_VERTICAL>`)
        DECIMALS					decimals in plotted values (see sFormatStr_GS for rules) (DEFAULT = 1)
        ANNOFF						annotation offset from bar (+/- determines side of the bar left/right and below/above)
        BOX_SIZE               box height (mm) (width for horizontal color bar) (DEFAULT = 4)
        BAR_WIDTH              width (mm) (short dimension) of the color bar (DEFAULT = 8)
        MINIMUM_GAP            Minimum space between annotations, otherwise drop annotations (DEFAULT = 0 mm)
        The actual height is over-estimated, so even with zero gap there will normally always be some space between labels.
        FIXED_INTERVAL         Preset interval for annotations scale (DEFAULT = DUMMY, use color zones)
        FIXED_MINOR_INTERVAL   Preset minor interval for annotations scale (DEFAULT = DUMMY, if defined must be 1/10, 1/5, 1/4 or 1/2 of FIXED_INTERVAL)
        X								X location	(REQUIRED)
        Y								Y location	(REQUIRED)
        POST_MAXMIN            Post limit values at ends of the bar (0 or 1)? (DEFAULT = 0)
        DIVISION_STYLE         One of MVU_DIVISION_STYLE_XXX (DEFAULT = `MVU_DIVISION_STYLE_LINES <geosoft.gxapi.MVU_DIVISION_STYLE_LINES>`)
        """
        gxapi_cy.WrapMVU.color_bar_reg(GXContext._get_tls_geo(), mview._wrapper, itr._wrapper, itr2._wrapper, reg._wrapper)
        



    @classmethod
    def contour(cls, mview, con, grid):
        """
        Creates a contour map.
        """
        gxapi_cy.WrapMVU.contour(GXContext._get_tls_geo(), mview._wrapper, con.encode(), grid.encode())
        



    @classmethod
    def contour_ply(cls, mview, ply, con, grid):
        """
        Creates a contour map with clipped areas.

        **Note:**

        The clipping `GXPLY <geosoft.gxapi.GXPLY>` can include a surrounding inclusive polygon
        and zero, one or more interior exclusive polygons. Construct
        a `GXPLY <geosoft.gxapi.GXPLY>` object using the `GXPLY.add_polygon_ex <geosoft.gxapi.GXPLY.add_polygon_ex>` function, to add both
        inclusive (as the first `GXPLY <geosoft.gxapi.GXPLY>`) and exclusive interior regions.
        """
        gxapi_cy.WrapMVU.contour_ply(GXContext._get_tls_geo(), mview._wrapper, ply._wrapper, con.encode(), grid.encode())
        



    @classmethod
    def c_symb_legend(cls, mview, x1, y1, font_size, symb_scale, file, title, sub_title):
        """
        Plot a legend for the classified color symbols.

        **Note:**

        If the symbol size, color, font etc are specified in
        the `GXITR <geosoft.gxapi.GXITR>`'s `GXREG <geosoft.gxapi.GXREG>`, then the Symbol scale factor is used
        allow the user to adjust the symbol sizes. They will be
        plotted at a size equal to the size in the `GXREG <geosoft.gxapi.GXREG>` times
        the scale factor.
        If no symbol size info can be found in the `GXREG <geosoft.gxapi.GXREG>`, then
        the symbol size is set equal to the Label Font Size.
        If no symbol font or number info is included in the
        `GXREG <geosoft.gxapi.GXREG>`, it is the programmer's responsibility to select
        the correct font and symbol before CSymbLegend is
        called. The same is true of the edge color.
        """
        gxapi_cy.WrapMVU.c_symb_legend(GXContext._get_tls_geo(), mview._wrapper, x1, y1, font_size, symb_scale, file.encode(), title.encode(), sub_title.encode())
        



    @classmethod
    def decay_curve(cls, mview, vv_x, vv_y, v_ay, v_ax, log, log_min, angle, x_bar, y_bar, x_off_set, y_off_set, width, height, x_min, y_min, x_scale, y_scale, line_pitch, line_style, line_color):
        """
        Plot decay curves at survey locations

        **Note:**

        Box width and height are used to draw horizontal and vertical
        bars. Curves outside the box are not clipped.
        """
        gxapi_cy.WrapMVU.decay_curve(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, v_ay._wrapper, v_ax._wrapper, log, log_min, angle, x_bar, y_bar, x_off_set, y_off_set, width, height, x_min, y_min, x_scale, y_scale, line_pitch, line_style, line_color.encode())
        



    @classmethod
    def direction_plot(cls, mview, vv_x, vv_y, size, loc, align):
        """
        Plot an arrow to indicate the direction of a flight line

        **Note:**

        An arrow will be drawn in the direction from the first valid
        to the last points in the X and Y VVs.
        """
        gxapi_cy.WrapMVU.direction_plot(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, size, loc, align)
        



    @classmethod
    def em_forward(cls, mview, xo, yo, size_x, size_y, coil_sep, coil_frequency, coil_configuration, r, h, i, q, rvv, hvv, ivv, qvv, lin_log, var):
        """
        Plot an EM forward model against inverted data.

        **Note:**

        This function is designed to display an inverted result beside
        the forward model curves. This is useful for trouble-shooting
        or understanding why a certain inversion result was obtained.
        The earth model is a simple halfspace.
        
        The forward model is plotted either as a function of
        resistivity at a single height, or as a function of height at
        a single resistivity. In either case, the relevant VVs must be
        completely filled (even if one is all the same value).
        """
        gxapi_cy.WrapMVU.em_forward(GXContext._get_tls_geo(), mview._wrapper, xo, yo, size_x, size_y, coil_sep, coil_frequency, coil_configuration, r, h, i, q, rvv._wrapper, hvv._wrapper, ivv._wrapper, qvv._wrapper, lin_log, var)
        



    @classmethod
    def export_datamine_string(cls, mview, lst, file):
        """
        Export selected map groups in a map view to a Datamine coordinate string file.

        **Note:**

        The lines, rectangles and polygons in the specified groups
        will be exported to a Datamine coordinate string (``*.dm``) file.
        The function attempts to duplicate the colors, etc. used.
        Complex polygon objects will be exported as independent
        single polygons.

        .. seealso::

            `GXLST <geosoft.gxapi.GXLST>` class
        """
        gxapi_cy.WrapMVU.export_datamine_string(GXContext._get_tls_geo(), mview._wrapper, lst._wrapper, file.encode())
        



    @classmethod
    def export_dxf_3d(cls, mview, lst, wa):
        """
        Export selected map groups in a map view to an AutoCAD 3D DXF file.

        **Note:**

        Supported objects exported include lines, polygons, text.

        .. seealso::

            `GXLST <geosoft.gxapi.GXLST>` class
        """
        gxapi_cy.WrapMVU.export_dxf_3d(GXContext._get_tls_geo(), mview._wrapper, lst._wrapper, wa._wrapper)
        



    @classmethod
    def export_surpac_str(cls, mview, lst, str_wa, styles_wa):
        """
        Export selected map groups in a map view to a Surpac `GXSTR <geosoft.gxapi.GXSTR>` file.

        **Note:**

        The lines, rectangles and polygons in the specified groups
        will be exported to a Surpac `GXSTR <geosoft.gxapi.GXSTR>` file. An accompanying styles
        file will be created which will attempt to duplicate the
        colors, etc. used.
        Complex polygon objects will be exported as independent
        single polygons.

        .. seealso::

            `GXLST <geosoft.gxapi.GXLST>` class
        """
        gxapi_cy.WrapMVU.export_surpac_str(GXContext._get_tls_geo(), mview._wrapper, lst._wrapper, str_wa._wrapper, styles_wa._wrapper)
        



    @classmethod
    def flight_plot(cls, mview, vv_x, vv_y, line, locate, vangle, up, loff, voff):
        """
        Draw a flight line

        **Note:**

        Current line color, thickness and style are used to
        draw the line.
        
        Current font, font color and font style are used to
        annotate the line labels.
        
        If current clipping is ON in the VIEW, lines will be
        clipped to the window before plotting.  In this case,
        labels should be located ABOVE or BELOW the line
        traces to prevent labels being clipped.
        
        The offsets dOffA and dOffB control the vertical and
        horizontal label offsets with respect to the ends of
        the line trace and depending on the label location.
        
        The vertical line reference angle dVerAng is used
        to determine if lines are considered vertical or
        horizontal.  Vertical lines use the sUp parameter
        to determine the label up direction.  Normally, use an
        angle of 60 degrees unless there are lines that run in
        this direction.

        .. seealso::

            `path_plot <geosoft.gxapi.GXMVU.path_plot>`
        """
        gxapi_cy.WrapMVU.flight_plot(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, line.encode(), locate, vangle, up, loff, voff)
        



    @classmethod
    def gen_areas(cls, mview, lines, col_vv, pat_vv, pitch):
        """
        Generate areas from an line group.

        **Note:**

        The specified line group will be used to create a new group that
        is composed of all the resolved polygonal areas in the line group.
        Each polygonal area is assigned a color/pattern as specified in the
        color and pattern `GXVV <geosoft.gxapi.GXVV>`'s.  Color/patterns are assigned in rotating
        sequence.

        .. seealso::

            `re_gen_areas <geosoft.gxapi.GXMVU.re_gen_areas>`
        """
        gxapi_cy.WrapMVU.gen_areas(GXContext._get_tls_geo(), mview._wrapper, lines.encode(), col_vv._wrapper, pat_vv._wrapper, pitch)
        



    @classmethod
    def get_range_gocad_surface(cls, file, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the XYZ range of a GOCAD surface.

        **Note:**

        Required to set up a map view before doing the actual
        surface import.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = gxapi_cy.WrapMVU.get_range_gocad_surface(GXContext._get_tls_geo(), file.encode(), min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        



    @classmethod
    def histogram(cls, mview, st_data, st_hist, title, unit, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, st_box):
        """
        Plot the histogram on a map.

        **Note:**

        This function just calls `histogram2 <geosoft.gxapi.GXMVU.histogram2>` with decimals set
        to -7 (7 significant figures).

        .. seealso::

            `histogram2 <geosoft.gxapi.GXMVU.histogram2>`, `histogram3 <geosoft.gxapi.GXMVU.histogram3>`
        """
        gxapi_cy.WrapMVU.histogram(GXContext._get_tls_geo(), mview._wrapper, st_data._wrapper, st_hist._wrapper, title.encode(), unit.encode(), xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, st_box._wrapper)
        



    @classmethod
    def histogram2(cls, mview, st_data, st_hist, x_title, y_title, xy_txt_size, title, plot_txt_size, unit, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, st_box, x_marker):
        """
        Plot the histogram on a map.

        **Note:**

        A vertical line through from bottom to top horizontal axis is drawn
        Also a label 'Threshold value' is plotted against this line. However,
        None of them will be plotted if threshold value is dummy or outside
        the X data range.
        """
        gxapi_cy.WrapMVU.histogram2(GXContext._get_tls_geo(), mview._wrapper, st_data._wrapper, st_hist._wrapper, x_title.encode(), y_title.encode(), xy_txt_size, title.encode(), plot_txt_size, unit.encode(), xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, st_box._wrapper, x_marker)
        



    @classmethod
    def histogram3(cls, mview, st_data, st_hist, title, unit, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, data_decimal, stat_decimal, st_box):
        """
        Plot the histogram on a map, specify decimals.
        """
        gxapi_cy.WrapMVU.histogram3(GXContext._get_tls_geo(), mview._wrapper, st_data._wrapper, st_hist._wrapper, title.encode(), unit.encode(), xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, fill_color, data_decimal, stat_decimal, st_box._wrapper)
        



    @classmethod
    def histogram4(cls, mview, st_data, st_hist, title, unit, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, prob, fill_color, data_decimal, stat_decimal, st_box):
        """
        As `histogram3 <geosoft.gxapi.GXMVU.histogram3>`, but allow probability scaling of percents.
        """
        gxapi_cy.WrapMVU.histogram4(GXContext._get_tls_geo(), mview._wrapper, st_data._wrapper, st_hist._wrapper, title.encode(), unit.encode(), xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, prob, fill_color, data_decimal, stat_decimal, st_box._wrapper)
        



    @classmethod
    def histogram5(cls, mview, st_data, st_hist, title, unit, lmd, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, prob, fill_color, data_decimal, stat_decimal, st_box, itr):
        """
        As `histogram4 <geosoft.gxapi.GXMVU.histogram4>`, but allow `GXITR <geosoft.gxapi.GXITR>` to color bars.

        **Note:**

        The `GXITR <geosoft.gxapi.GXITR>` can be empty (but must still be a valid `GXITR <geosoft.gxapi.GXITR>` object).
        """
        gxapi_cy.WrapMVU.histogram5(GXContext._get_tls_geo(), mview._wrapper, st_data._wrapper, st_hist._wrapper, title.encode(), unit.encode(), lmd, xm, ym, widthm, heightm, xd, yd, widthd, heightd, sum_width, log, summ, prob, fill_color, data_decimal, stat_decimal, st_box._wrapper, itr._wrapper)
        



    @classmethod
    def exportable_dxf_3d_groups_lst(cls, mview, lst):
        """
        Return a `GXLST <geosoft.gxapi.GXLST>` of groups you can export using sExportDXF3D_MVU.

        **Note:**

        Returns a list of visible groups that the DXF 3D export can
        export. Removes things like `GXVOXD <geosoft.gxapi.GXVOXD>`, `GXAGG <geosoft.gxapi.GXAGG>`, and target
        groups starting with "Dh", which are typically plotted in 3D
        views on a reference plan oriented toward the user, and thus
        not exportable.
        """
        ret_val = gxapi_cy.WrapMVU.exportable_dxf_3d_groups_lst(GXContext._get_tls_geo(), mview._wrapper, lst._wrapper)
        return ret_val



    @classmethod
    def mapset_test(cls, min_x, max_x, min_y, max_y, size, port, exact, scale, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside):
        """
        Test function to ensure parameters to `mapset <geosoft.gxapi.GXMVU.mapset>` is sane

        **Note:**

        Use `GXSYS.show_error <geosoft.gxapi.GXSYS.show_error>` to display errors that may have been encountered. This function can also be used
        to calculate the default scale without creating a map.
        """
        ret_val, scale.value = gxapi_cy.WrapMVU.mapset_test(GXContext._get_tls_geo(), min_x, max_x, min_y, max_y, size.encode(), port, exact, scale.value, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside)
        return ret_val



    @classmethod
    def mapset2_test(cls, min_x, max_x, min_y, max_y, size, port, exact, scale, vert_exag, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside):
        """
        Test function to ensure parameters to `mapset <geosoft.gxapi.GXMVU.mapset>` is sane

        **Note:**

        Same as `mapset_test <geosoft.gxapi.GXMVU.mapset_test>`, with vertical exaggeration.
        """
        ret_val, scale.value = gxapi_cy.WrapMVU.mapset2_test(GXContext._get_tls_geo(), min_x, max_x, min_y, max_y, size.encode(), port, exact, scale.value, vert_exag, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside)
        return ret_val



    @classmethod
    def import_gocad_surface(cls, mview, file, col):
        """
        Import and plot a GOCAD surface model.

        **Note:**

        The vertex normals are not included in the
        GOCAD import, but are calculated using
        the normal of each defined triangle, and taking the
        average when vertex is shared among more than one triangle.
        """
        gxapi_cy.WrapMVU.import_gocad_surface(GXContext._get_tls_geo(), mview._wrapper, file.encode(), col)
        



    @classmethod
    def load_plot(cls, map, name):
        """
        Load a Geosoft PLT file into a `GXMAP <geosoft.gxapi.GXMAP>`.
        """
        gxapi_cy.WrapMVU.load_plot(GXContext._get_tls_geo(), map._wrapper, name.encode())
        



    @classmethod
    def map_from_plt(cls, map, base, data, plt, mpx, mpy):
        """
        Creates a new map from a PLT file.

        **Note:**

        This only creates a map, it does not read the PLT into
        the map.  The base view and data view will be the same
        size.

        .. seealso::

            `load_plot <geosoft.gxapi.GXMVU.load_plot>`
        """
        gxapi_cy.WrapMVU.map_from_plt(GXContext._get_tls_geo(), map._wrapper, base.encode(), data.encode(), plt.encode(), mpx, mpy)
        



    @classmethod
    def map_mdf(cls, map, mdf, data):
        """
        Creates an MDF from a Map.
        """
        gxapi_cy.WrapMVU.map_mdf(GXContext._get_tls_geo(), map._wrapper, mdf.encode(), data.encode())
        



    @classmethod
    def mapset(cls, map, base, data, min_x, max_x, min_y, max_y, size, port, exact, scale, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside):
        """
        Creates a new map directly from parameters.
        """
        gxapi_cy.WrapMVU.mapset(GXContext._get_tls_geo(), map._wrapper, base.encode(), data.encode(), min_x, max_x, min_y, max_y, size.encode(), port, exact, scale, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside)
        



    @classmethod
    def mapset2(cls, map, base, data, min_x, max_x, min_y, max_y, size, port, exact, scale, vert_exag, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside):
        """
        Same as `mapset <geosoft.gxapi.GXMVU.mapset>`, with vertical exaggeration.
        """
        gxapi_cy.WrapMVU.mapset2(GXContext._get_tls_geo(), map._wrapper, base.encode(), data.encode(), min_x, max_x, min_y, max_y, size.encode(), port, exact, scale, vert_exag, conv, marg_xmin, marg_xmax, marg_ymin, marg_ymax, inside)
        



    @classmethod
    def mdf(cls, map, mdf, base, data):
        """
        Creates a new map from an MDF file.
        """
        gxapi_cy.WrapMVU.mdf(GXContext._get_tls_geo(), map._wrapper, mdf.encode(), base.encode(), data.encode())
        



    @classmethod
    def path_plot(cls, mview, vv_x, vv_y, line, locate, vangle, up, loff, voff, gap):
        """
        Draw a flight line

        **Note:**

        See `flight_plot <geosoft.gxapi.GXMVU.flight_plot>`.  This is the same except for the
        additional line gap parameter.

        .. seealso::

            FlighPlot_MVU
        """
        gxapi_cy.WrapMVU.path_plot(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, line.encode(), locate, vangle, up, loff, voff, gap)
        



    @classmethod
    def path_plot_ex(cls, mview, vv_x, vv_y, line, locate, compass, vangle, up, loff, voff, gap):
        """
        Draw a flight line

        **Note:**

        This is the same except for the additional line compass parameter.

        .. seealso::

            `path_plot <geosoft.gxapi.GXMVU.path_plot>`
        """
        gxapi_cy.WrapMVU.path_plot_ex(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, line.encode(), locate, compass, vangle, up, loff, voff, gap)
        



    @classmethod
    def path_plot_ex2(cls, mview, vv_x, vv_y, line, locate, compass, vangle, up, loff, voff, gap, dummies):
        """
        Draw a flight line

        **Note:**

        This is the same except for the additional line dummies parameter.

        .. seealso::

            `path_plot_ex <geosoft.gxapi.GXMVU.path_plot_ex>`
        """
        gxapi_cy.WrapMVU.path_plot_ex2(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, line.encode(), locate, compass, vangle, up, loff, voff, gap, dummies)
        



    @classmethod
    def plot_voxel_surface(cls, mview, vox, value, col, line_thick):
        """
        Extract an iso-surface from a voxel and plot it to a 2D or 3D view.

        **Note:**

        The Marching Cubes method of Lorensen and Cline, Computer Graphics, V21,
        Number 4, July 1987, is used to calculate a given iso-surface in a voxel
        model. The resulting surface is plotted to a 2D or 3D view. If the view
        is 2-D, then only the intersection of the surface with the 2D surface is
        plotted, using lines.
        """
        gxapi_cy.WrapMVU.plot_voxel_surface(GXContext._get_tls_geo(), mview._wrapper, vox._wrapper, value, col, line_thick)
        



    @classmethod
    def plot_voxel_surface2(cls, mview, vox, value, col, line_thick, transparency, surface_name):
        """
        Extract an iso-surface from a voxel and plot it to a 2D or 3D view.

        **Note:**

        The Marching Cubes method of Lorensen and Cline, Computer Graphics, V21,
        Number 4, July 1987, is used to calculate a given iso-surface in a voxel
        model. The resulting surface is plotted to a 2D or 3D view. If the view
        is 2-D, then only the intersection of the surface with the 2D surface is
        plotted, using lines.
        """
        gxapi_cy.WrapMVU.plot_voxel_surface2(GXContext._get_tls_geo(), mview._wrapper, vox._wrapper, value, col, line_thick, transparency, surface_name.encode())
        



    @classmethod
    def generate_surface_from_voxel(cls, mview, vox, method, option, min_value, max_value, col, line_thick, transparency, surface_name):
        """
        TODO...

        **Note:**

        TODO... Move to `GXVOX <geosoft.gxapi.GXVOX>` method for surface generation only and use GeosurfaceD to display.
        """
        gxapi_cy.WrapMVU.generate_surface_from_voxel(GXContext._get_tls_geo(), mview._wrapper, vox._wrapper, method, option, min_value, max_value, col, line_thick, transparency, surface_name.encode())
        



    @classmethod
    def post(cls, mview, vv_x, vv_y, vv_z, dummy, size, format, decimals, ref, angle):
        """
        Post values on a map.
        """
        gxapi_cy.WrapMVU.post(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, dummy, size, format, decimals, ref, angle)
        



    @classmethod
    def post_ex(cls, mview, vv_x, vv_y, vv_z, vv_s, dummy, base, min_detect, size, format, decimals, offset_l, offset_p, alternate, mod, ref, angle, fixed, ref_ang, up):
        """
        Post values on a map with more paramters.
        """
        gxapi_cy.WrapMVU.post_ex(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_s._wrapper, dummy, base, min_detect, size, format, decimals, offset_l, offset_p, alternate, mod, ref, angle, fixed, ref_ang, up)
        



    @classmethod
    def probability(cls, mview, st_data, st_hist, title, unit, transform, lmd, xm, ym, widthm, heightm, symb_size, sigma, sum_width, summ, data_decimal, stat_decimal, itr):
        """
        Plot a probability plot on a map.

        **Note:**

        The `GXITR <geosoft.gxapi.GXITR>` can be empty (but must still be a valid `GXITR <geosoft.gxapi.GXITR>` object).
        """
        gxapi_cy.WrapMVU.probability(GXContext._get_tls_geo(), mview._wrapper, st_data._wrapper, st_hist._wrapper, title.encode(), unit.encode(), transform, lmd, xm, ym, widthm, heightm, symb_size, sigma, sum_width, summ, data_decimal, stat_decimal, itr._wrapper)
        



    @classmethod
    def profile_plot(cls, mview, vv_x, vv_y, vv_z, vangle, up, gap, base, scale, join):
        """
        Draw a profile along line trace

        **Note:**

        Profiles will be drawn in the current line style.
        """
        gxapi_cy.WrapMVU.profile_plot(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vangle, up, gap, base, scale, join)
        



    @classmethod
    def profile_plot_ex(cls, mview, vv_x, vv_y, vv_z, vangle, up, gap, base, scale, join, log, log_base, smooth, pos_f_color, neg_f_color):
        """
        Draw a profile along line trace with more parameters

        **Note:**

        Profiles will be drawn in the current line style.
        """
        gxapi_cy.WrapMVU.profile_plot_ex(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vangle, up, gap, base, scale, join, log, log_base, smooth, pos_f_color.encode(), neg_f_color.encode())
        



    @classmethod
    def prop_symb_legend(cls, mview, x1, y1, font_size, symb_scale, base, n_symb, start, increment, title, sub_title):
        """
        Draw a legend for proportional symbols.

        **Note:**

        All symbol attributes, except for the size, are assumed
        to be defined (or defaults are used).
        Spacing is based on the maximum of the largest plotted symbol
        and the font size.
        """
        gxapi_cy.WrapMVU.prop_symb_legend(GXContext._get_tls_geo(), mview._wrapper, x1, y1, font_size, symb_scale, base, n_symb, start, increment, title.encode(), sub_title.encode())
        



    @classmethod
    def re_gen_areas(cls, mview, lines):
        """
        Re-Generate from a line group and existing area group

        **Note:**

        The area group must exist and will be modified to match the current
        line group.
        
        All non-polygon entities in the current area group will remain in the
        new area group.  All existing polygon groups will be used to determine
        the most likely attributes for the new polygon groups.
        
        There must be existing polygon groups in the area group.

        .. seealso::

            `gen_areas <geosoft.gxapi.GXMVU.gen_areas>`
        """
        gxapi_cy.WrapMVU.re_gen_areas(GXContext._get_tls_geo(), mview._wrapper, lines.encode())
        



    @classmethod
    def symb_off(cls, mview, vv_x, vv_y, vv_f, x_off, y_off):
        """
        Draws symbols with an offset and against a flag channel

        **Note:**

        Symbols are not plotted for positions where the flag `GXVV <geosoft.gxapi.GXVV>`
        value is 0 or `iDUMMY <geosoft.gxapi.iDUMMY>`.
        """
        gxapi_cy.WrapMVU.symb_off(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, vv_f._wrapper, x_off, y_off)
        



    @classmethod
    def text_box(cls, mview, xmin, ymin, xmax, ymax, text, space, type):
        """
        Draw a wrapped text box
        """
        gxapi_cy.WrapMVU.text_box(GXContext._get_tls_geo(), mview._wrapper, xmin, ymin, xmax, ymax, text.encode(), space, type)
        



    @classmethod
    def tick(cls, mview, vv_x, vv_y, vv_s, size, mod, mt_size, mt_mod):
        """
        Draw line ticks on a map.
        """
        gxapi_cy.WrapMVU.tick(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, vv_s._wrapper, size, mod, mt_size, mt_mod)
        



    @classmethod
    def tick_ex(cls, mview, vv_x, vv_y, vv_s, size, mod, mt_size, mt_mod, gap):
        """
        Same as `tick <geosoft.gxapi.GXMVU.tick>`, with gap allowance.
        """
        gxapi_cy.WrapMVU.tick_ex(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, vv_s._wrapper, size, mod, mt_size, mt_mod, gap)
        



    @classmethod
    def trnd_path(cls, mview, vv_x, vv_y, min_sect, min_dist):
        """
        Plot min and max trend lines.

        **Note:**

        Trend lines positions consist of X and Y VVs
        interspersed with dummies, which separate the
        individual trend sections.
        Set the minimum number of sections to > 0 to
        plot only the longer trend lines.
        (The number of sections in one trend section is
        equal to the number of points between dummies minus one.)
        Set the minimum distance to > 0 to
        plot only the longer trend lines.
        """
        gxapi_cy.WrapMVU.trnd_path(GXContext._get_tls_geo(), mview._wrapper, vv_x._wrapper, vv_y._wrapper, min_sect, min_dist)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer